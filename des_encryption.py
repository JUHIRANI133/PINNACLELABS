from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def des_encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted = cipher.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(encrypted).decode()

def des_decrypt(cipher_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decoded = base64.b64decode(cipher_text)
    decrypted = cipher.decrypt(decoded).decode('utf-8')
    return decrypted.strip()


 