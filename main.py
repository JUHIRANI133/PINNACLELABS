from aes_encryption import aes_encrypt, aes_decrypt
from des_encryption import des_encrypt, des_decrypt
from rsa_encryption import generate_keys, rsa_encrypt, rsa_decrypt

print("==== TEXT ENCRYPTION TOOL ====\n")

text = input("Enter text to encrypt: ")

print("\n--- AES Encryption ---")
aes_key = b'ThisIsASecretKey'
aes_cipher = aes_encrypt(text, aes_key)
print("Encrypted (AES):", aes_cipher)
print("Decrypted (AES):", aes_decrypt(aes_cipher, aes_key))

print("\n--- DES Encryption ---")
des_key = b'8bytekey'
des_cipher = des_encrypt(text, des_key)
print("Encrypted (DES):", des_cipher)
print("Decrypted (DES):", des_decrypt(des_cipher, des_key))

print("\n--- RSA Encryption ---")
public_key, private_key = generate_keys()
rsa_cipher = rsa_encrypt(text, public_key)
print("Encrypted (RSA):", rsa_cipher)
print("Decrypted (RSA):", rsa_decrypt(rsa_cipher, private_key))
 