from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def aes_encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted = cipher.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(encrypted).decode()

def aes_decrypt(cipher_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decoded = base64.b64decode(cipher_text)
    decrypted = cipher.decrypt(decoded).decode('utf-8')
    return decrypted.strip()

