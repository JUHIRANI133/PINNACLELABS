from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

BLOCK_SIZE = 16  


def pad(data):
    padding_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([padding_len]) * padding_len

def unpad(data):
    padding_len = data[-1]
    return data[:-padding_len]


def encrypt_image(file_path, key, output_path):
    with open(file_path, 'rb') as f:
        image_data = f.read()

    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(image_data))

    with open(output_path, 'wb') as f:
        f.write(iv + encrypted_data)


def decrypt_image(encrypted_path, key, output_path):
    with open(encrypted_path, 'rb') as f:
        encrypted_data = f.read()

    iv = encrypted_data[:BLOCK_SIZE]
    cipher_data = encrypted_data[BLOCK_SIZE:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(cipher_data))

    with open(output_path, 'wb') as f:
        f.write(decrypted_data)
