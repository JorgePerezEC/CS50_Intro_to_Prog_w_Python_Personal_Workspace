from project import cipher_key_gen, encrypt_item, decrypt_item
import hashlib
from cryptography.fernet import Fernet, InvalidToken
import pytest

def test_cipher_key_gen():
    test_password = "my_test_password".encode('utf-8')
    hashed_password = hashlib.sha256(test_password).digest()

    cipher = cipher_key_gen(hashed_password)

    # Fernet instance verify
    assert isinstance(cipher, Fernet)

def test_encrypt_item():
    key = Fernet.generate_key()
    cipher_test = Fernet(key)

    plaintext = "Hello world"
    encrypted_text = encrypt_item(cipher_test, plaintext)

    assert encrypted_text is not None

def test_decrypt_item():
    key = Fernet.generate_key()
    cipher_test = Fernet(key)
    plaintext = "Hello, world!"
    encrypted_text = encrypt_item(cipher_test, plaintext)
    decrypted_text = decrypt_item(cipher_test, encrypted_text)

    assert decrypted_text == plaintext

def test_decrypt_item_fail():
    key = Fernet.generate_key()
    cipher_test = Fernet(key)
    plaintext = "Hello, world!"
    encrypted_text = encrypt_item(cipher_test, plaintext)

    # Create another key
    key2 = Fernet.generate_key()
    cipher_test2 = Fernet(key2)
    # Try to decrypt using another key
    with pytest.raises(InvalidToken):
        decrypt_item(cipher_test2, encrypted_text)
