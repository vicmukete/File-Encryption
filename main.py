from cryptography.fernet import Fernet
import os

# Initial Documentation Sample Code
'''key1 = Fernet.generate_key()
f = Fernet(key1)
token = f.encrypt(b'What i want to encrypt')
print(token)
clear = f.decrypt(token)
print(clear.decode())'''


# encrypt a single folder
def encrypt_file(key, filename):
    with open(filename, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    # token
    encrypted_data = fernet.encrypt(data)
    with open(filename + '.enc', 'wb') as file:
        file.write(encrypted_data)


# encrypt all files in the folder
def encrypt_folder(key, folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            filepath = os.path.join(root, file)
            # specifications for this specific file
            # all wi-fi pws will be encrypted
            if '.xml' in file:
                print(file)
                encrypt_file(key, filepath)


# decrypt a single file
def decrypt_file(key, filename):
    with open(filename, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data)

    with open(filename, 'wb') as file:
        file.write(decrypted_data)


# decrypt the entire folder
def decrypt_folder(key, folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            filepath = os.path.join(root, file)
            if '.enc' in file:
                print(file)
                decrypt_file(key, filepath)


folderPath = r'C:\Users\muket\Desktop\Projects\Unethical\WiFi PWs'


# Saves the encryption/decryption key
key_path = r'C:\Users\muket\Desktop\Real Projects\File Encryption\key.key'

if not os.path.exists(key_path):
    fernetKey = Fernet.generate_key()
    with open(key_path, 'wb') as key_file:
        key_file.write(fernetKey)
else:
    with open(key_path, 'rb') as key_file:
        fernetKey = key_path


while True:
    try:
        encryptOrDecrypt = input(
            'Would you like to encrypt or decrypt your folder [e (encrypt) or d (decrypt)]: ').lower()
        if encryptOrDecrypt == 'e':
            encrypt_folder(fernetKey, folderPath)
            print('Complete :)')
            break
        elif encrypt_file == 'd':
            decrypt_folder(fernetKey, folderPath)
            print('Complete :)')
            break
    except SyntaxError:
        print('Please enter a valid response')
