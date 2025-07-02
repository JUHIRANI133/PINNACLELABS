from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return public_key, private_key

def rsa_encrypt(plain_text, public_key_bytes):
    public_key = RSA.import_key(public_key_bytes)
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(plain_text.encode('utf-8'))
    return base64.b64encode(encrypted).decode()

def rsa_decrypt(cipher_text, private_key_bytes):
    private_key = RSA.import_key(private_key_bytes)
    cipher = PKCS1_OAEP.new(private_key)
    decrypted = cipher.decrypt(base64.b64decode(cipher_text))
    return decrypted.decode('utf-8')
 