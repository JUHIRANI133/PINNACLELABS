from image_encryptor import encrypt_image, decrypt_image
import os


key = b"ThisIsASecretKey"

print(" Image Encryption Tool")
print("========================")

choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? ").lower()

if choice == 'e':
    input_path = r"C:\PROGRAMMING\CYBERSECURITY\TASK03\secure_image.png"
            
    output_path = 'encrypted_image.enc'
    encrypt_image(input_path, key, output_path)
    print(f"\n Image encrypted successfully as '{output_path}'")

elif choice == 'd':
    input_path = 'encrypted_image.enc'
    output_path = 'decrypted_image.png'         
    decrypt_image(input_path, key, output_path)
    print(f"\n Image decrypted successfully as '{output_path}'")

else:
    print(" Invalid choice. Please enter 'e' or 'd'.")
