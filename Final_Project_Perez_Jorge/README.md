# 🔐PASSWORD MANAGER (Multi-users) - CS50 Final Project
### Introduction
This project is a password manager developed in Python using libraries such as bcrypt and cryptography to encrypt and decrypt sensitive data, such as passwords. The program operates solely through the command line and offers a set of functionalities for securely managing passwords for more than one user.
##### ▶️Video Demo:  <[URL HERE](https://youtu.be/pP_-qgMyTRE)>
##### Made by Jorge Pérez
### Description:

The program starts by prompting the user to enter their username. If the user is not registered, they will be asked to create a secure password, which will be validated using the password_strength library. This password is securely stored using bcrypt and saved in a file called key.csv, which contains the hash of the password for added security.

Once the user is registered or logged in, the following options are presented:

**1. Add New Password:** Allows the user to store a new password for a specific website.

**2. Remove Stored Password:** Enables the user to delete a previously stored password.

**3. List Stored Passwords:** Displays all passwords stored by the user.

**4. Exit:** Exit the program.
### 🔐Security
All users are stored in the main file (key.csv), where the hash of their password is securely stored. This approach allows for multiple users without the need for separate files, while ensuring that each user can only access their own passwords.

To encrypt and decrypt passwords, a process is used that involves generating a unique salt for each user. This salt is generated based on the hash of the user's password, ensuring that passwords can only be encrypted and decrypted if the corresponding user's password is known.

In addition to the robust encryption mechanisms, the application prioritizes user confidentiality by incorporating the pwinput library. This library allows passwords entered by users to be concealed from the console, thereby preventing potential shoulder surfing attacks or unauthorized access to sensitive information. By masking password inputs, the application ensures an extra layer of security, enhancing the overall privacy of the user's interactions with the system.

### 🗂️Files
**🐍project.py:** Contains the main code of the program, including the logic for handling the different menu options.

**🐍utils.py:** Contains functions related to password management, such as store and load the salt, etc.

**🐍test_project.py:** Contains tests.

**📋key.csv:** File that stores the hashes of users' passwords for authentication purposes.

**📃[hash]_salt.txt:** File that stores the encypted salt generated per every user.

**📃requeriments.txt:**  pip-installable libraries

#### 🔑Encypt function
The function cipher_key_gen, generates or retrieves the respective salt file based on the hashed password of the user, which is hashed again using the SHA256 algorithm. This adds an extra layer of security to prevent the compromise of stored passwords.

Here's how it works:

**1.Generating a Secure File Name:** The function first generates a secure and unique file name for the salt by hashing the provided password using the SHA256 algorithm and appending '_salt.txt' to it.

**2.Checking for Existing Salt File:** It checks if the salt file with the generated file name already exists. If it does, it loads the salt from the file.

**3.Generating Random Salt:** If the salt file doesn't exist, it generates a random salt using os.urandom(16).

**4.Storing the Salt:** In either case, whether the salt file exists or not, the function stores the salt in the respective file.

**5.Deriving the Key:** It then derives the encryption key using PBKDF2 with the hashed password and the loaded or generated salt. PBKDF2 ensures that the key derivation is slow, making it resistant to brute-force attacks.

**6.Creating the Cipher:** Finally, it creates a Fernet cipher using the derived key.

By associating the salt file with the hashed password of the user, the function enhances security by ensuring that each user's salt is unique and not shared across different users. This mitigates the risk of password compromise even if the stored hashes are somehow accessed by an attacker.


Additionally, each time the program is executed, it dynamically creates a Fernet key based on the hash of the user's password. This means that even if the same user logs in multiple times, a unique encryption key is generated for them every time, enhancing the security of the password storage system. By dynamically deriving the encryption key from the hashed password, the system ensures that the encryption process is robust and tailored to each user's credentials, thereby further safeguarding the confidentiality of stored passwords.





