import sys, os
import bcrypt #Library to encrypt passwords and files
from password_strength import PasswordPolicy #Library to verify password strength
import pandas as pd
import pwinput #Library to hide passwords in console
from tabulate import tabulate
import hashlib
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from utils import decrypt_item_safe, clear_console, load_salt, store_salt

# Verify strength of password
policy = PasswordPolicy.from_names(
    length=5,  # min length: 5
    uppercase=1,  # need min. 1 uppercase letters
    numbers=1,  # need min. 1 digits
    special=1,  # need min. 1 special characters
    nonletters=2,  # need min. 1 non-letter characters (digits, specials, anything)
)

def cipher_key_gen(hashed_password):
    # Use a hash function to create a secure and unique file name for the salt
    salt_filename = hashlib.sha256(hashed_password).hexdigest() + '_salt.txt'
    if os.path.exists(salt_filename):
        # Load the salt from the file
        salt = load_salt(salt_filename)

    else:
        # Generate a random salt
        salt = os.urandom(16)
        # Store the salt in a file
        store_salt(salt, salt_filename)
        print("Salt generated - Keep it safe")
        print("Filename:", salt_filename)

    # Derive the key using PBKDF2 with the hashed password and the loaded salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 32 bytes
        salt=salt,
        iterations=100000,  # Number of iterations
        backend=default_backend()
    )
    key = kdf.derive(hashed_password)

    cipher = Fernet(base64.urlsafe_b64encode(key))

    return cipher


# Function to encrypt a  password.
def encrypt_item(cipher, item):
   return cipher.encrypt(item.encode()).decode()

# Function to decrypt a  password.
def decrypt_item(cipher, encrypted_item):
   return cipher.decrypt(encrypted_item.encode()).decode()

def main():

    try:
        # Load existing DataFrame or create a new one to store hash keys
        try:
            key_df = pd.read_csv("key.csv", index_col=None)
            if key_df.empty:
                key_df = pd.DataFrame(columns=["ID","User Name", "Encrypted Key"])

        except FileNotFoundError:
            key_df = pd.DataFrame(columns=["ID", "User Name", "Encrypted Key"])

        print("\n###################################################")
        print("                 [CS50 FINAL PROJECT]               ")
        print(" ######### 🔐 PERSONAL PASSWORD MANAGER 🔐 #########")
        print("###################################################\n")

        while True:
            account = input("Please, enter User name: ").strip()

            # Search if user exists
            user_entry = key_df.loc[key_df["User Name"] == account]
            if not user_entry.empty:
                break
            else:
                answ = input("User not registered. Do you want to register?(y/n) ")
                if answ == "y" or answ =="Y":
                    print("")
                    break
                else:
                    print("")
                    continue

        if not user_entry.empty:
            #User already registered
            user_key_restored = user_entry.iloc[0]["Encrypted Key"]
            user_key_restored = str(user_key_restored).encode('utf-8')

            while True:
                print("--------------------\n      LOG IN\n--------------------")
                passcode_usr = pwinput.pwinput(prompt='Enter your Password: ')
                passcode_usr = str(passcode_usr).strip().encode('utf-8')

                #Validate user password
                if bcrypt.checkpw(passcode_usr, user_key_restored):
                    print("✅ Successful login")
                    passcode_usr = user_key_restored
                    break
                else:
                    print("⚠️ Wrong password. Try again.")

        else: #REGISTER NEW USER
            print("NEW USER")
            while True:
                #New user
                last_id = key_df["ID"].max()
                new_id = last_id + 1 if not pd.isna(last_id) else 1

                print("Please, create a new password with the following characteristics:")
                print("  - Minimum length: 5")
                print("  - Need minimum 1 uppercase letter")
                print("  - Need minimum 1 digits")
                print("  - Need minimum 1 special characters (Example: $, #, %, &, ...)\n")
                passcode = pwinput.pwinput(prompt='New password: ')
                confirm_passcode = pwinput.pwinput("Confirm Password: ")

                if passcode == confirm_passcode:
                    if len(policy.test(passcode)) == 0:
                        user_key = bcrypt.hashpw(passcode.encode('utf-8'), bcrypt.gensalt())
                        passcode_usr = user_key
                        new_entry = pd.DataFrame([{"ID": int(new_id), "User Name": account,
                                            "Encrypted Key": passcode_usr.decode('utf-8'),
                        }])

                        key_df = pd.concat([key_df, new_entry], ignore_index=True)
                        key_df = key_df[["ID", "User Name", "Encrypted Key"]]
                        key_df.to_csv("key.csv", index=False)
                        clear_console()
                        print("\n------------User created------------\n")
                        print(f"Username: {account}")
                        break
                    else:
                        print("🚨 Password does not meet the following characteristics:", policy.test(passcode))
                        print("Try again.\n")
                else:
                    print("----------------------------\n!!!Error password does not match!!!----------------------------")
                    print("Please, try again\n")

        # Load existing DataFrame or create a new one
        try:
            pass_df = pd.read_csv("passwords.csv", index_col=None)
        except FileNotFoundError:
            pass_df = pd.DataFrame(columns=["ID", "Account Hash", "Website Name", "Username Name", "Encrypted Password"])


        cipher_obj = cipher_key_gen(passcode_usr)

        while True:
            option = menu()
            try:
                match option:
                    case "1":
                        last_id_psw = pass_df["ID"].max()
                        new_id_psw = last_id_psw + 1 if not pd.isna(last_id_psw) else 1

                        website_name = input("Website Name: ").strip()
                        user_name = input("User name or Email: ").strip()
                        password_site  = pwinput.pwinput(prompt='Website password: ')
                        encrypted_account = encrypt_item(cipher_obj, account)
                        encrypted_passcode = encrypt_item(cipher_obj, password_site)

                        new_entry = pd.DataFrame([{"ID": int(new_id_psw), "Account Hash": encrypted_account,
                                                "Website Name": website_name, "User Name": user_name,
                                                "Encrypted Password": encrypted_passcode
                        }])
                        pass_df = pd.concat([pass_df, new_entry], ignore_index=True)
                        pass_df = pass_df[["ID", "Account Hash","Website Name", "User Name", "Encrypted Password"]]
                        pass_df.to_csv("passwords.csv", index=False)
                        print("\n------------Password stored------------\n")
                        # break
                    case "2":
                        pass_df_copy = pass_df.copy()
                        pass_df_copy["Decrypted Account Hash"] = pass_df_copy["Account Hash"].apply(lambda x: decrypt_item_safe(cipher_obj, x))
                        pass_df_copy["Password"] = "*******"
                        pass_df_copy = pass_df_copy.loc[pass_df_copy["Decrypted Account Hash"] == account]
                        pass_df_copy.drop(columns=['Account Hash', 'Encrypted Password', 'Decrypted Account Hash'], axis=1, inplace=True)
                        if len(pass_df_copy) != 0:
                            print(tabulate(pass_df_copy, headers='keys', tablefmt='pretty', showindex=False))
                            web_site = input("Enter Website name to delete: ").strip()
                            #Filter to delete when string contains the same word and the same numbers of characters
                            filtered_df = pass_df_copy[(pass_df_copy['Website Name'] != web_site) &
                                                       (pass_df_copy['Website Name'].str.len() != len(web_site))]

                            if len(filtered_df) < len(pass_df_copy):
                                id_anteriores = pass_df_copy["ID"].tolist()
                                ids_news = filtered_df["ID"].tolist()
                                ids_to_delete = list(set(id_anteriores) - set(ids_news))
                                print(ids_to_delete)
                                pass_df = pass_df[~pass_df["ID"].isin(ids_to_delete)]
                                pass_df.to_csv("passwords.csv", index=False)
                                print("\n✅ Register deleted.")
                                # print(tabulate(filtered_df, headers='keys', tablefmt='pretty', showindex=False))
                            else:
                                print("Message: The website entered is not registered.\n")

                        else:
                            print("Message: No passwords saved.\n")
                    case "3":
                        print("\n------------LIST ALL STORED PASSWORDS------------\n")
                        print("#########################################################")
                        # Desencriptar todos los hashes almacenados en el DataFrame
                        pass_df_copy = pass_df.copy()
                        pass_df_copy["Decrypted Account Hash"] = pass_df_copy["Account Hash"].apply(lambda x: decrypt_item_safe(cipher_obj, x))
                        pass_df_copy["Decrypted Password"] = pass_df_copy["Encrypted Password"].apply(lambda x: decrypt_item_safe(cipher_obj, x))

                        # Filtrar las filas donde el hash desencriptado coincide con la cuenta deseada
                        rows_filtered = pass_df_copy.loc[pass_df_copy["Decrypted Account Hash"] == account]
                        filtered_df_copy = rows_filtered.copy()
                        filtered_df_copy.drop(['Account Hash', 'Decrypted Account Hash', 'Encrypted Password'], axis=1, inplace=True)

                        if len(filtered_df_copy) != 0:
                            print(tabulate(filtered_df_copy, headers='keys', tablefmt='pretty', showindex=False))
                        else:
                            print("Message: No passwords saved.")
                        print("#########################################################")

                    case "4":
                        clear_console()
                        sys.exit("Good bye. 👌")

                    case _:
                        print("Wrong option selected.\n")
            except Exception as ex:
                print("Exception:", ex)

    except KeyboardInterrupt:
        clear_console()
        print("Exit password manager")
    except Exception as ex:
        sys.exit("Exception:", ex)


def menu():
    while True:
        try:
            print("----------------------------\n    MENU    \n----------------------------\n")
            print("[1]. Add site password")
            print("[2]. Remove site password")
            print("[3]. List all stored passwords")
            print("[4]. Exit")
            opc = input("Option: ")
            return opc
        except Exception as ex:
            print("Error:", ex)


if __name__ == "__main__":
    main()
