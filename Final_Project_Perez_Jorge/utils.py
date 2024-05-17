import os

def store_salt(salt, filename):
    with open(filename, 'wb') as salt_file:
        salt_file.write(salt)

def load_salt(filename):
    with open(filename, 'rb') as salt_file:
        return salt_file.read()

def decrypt_item_safe(cipher, encrypted_item):
    try:
        return cipher.decrypt(encrypted_item.encode()).decode()
    except Exception as e:
        return None

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
