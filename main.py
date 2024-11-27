from cryptography.fernet import Fernet
import os

folderPath = r'C:\Users\muket\Desktop\Projects\Unethical\WiFi PWs'

# Saves the encryption/decryption key
key_path = r'C:\Users\muket\Desktop\Real Projects\File Encryption\key.key'

if not os.path.exists(key_path):
    fernetKey = Fernet.generate_key()
    with open(key_path, 'wb') as key_file:
        key_file.write(fernetKey)
else:
    with open(key_path, 'rb') as key_file:
        fernetKey = key_file.read()

fernet = Fernet(fernetKey)


# encrypt a single folder
def encrypt_file(filename):
    # open the file as binary because the
    # Fernet class requires it to function
    with open(filename, 'rb') as file:
        data = file.read()

    # token
    encrypted_data = fernet.encrypt(data)

    # here the file extensions is changed when the file is encrypted
    # this is make sure that ik which files have already been encrypted
    new_filename = filename.replace(".xml", ".enc")
    with open(new_filename, 'wb') as file:
        file.write(encrypted_data)
    os.remove(filename)


# encrypt all files in the folder
def encrypt_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            filepath = os.path.join(root, file)
            # specifications for this specific file
            # all wi-fi pws will be encrypted
            if '.xml' in file:
                print(file)
                print(f'Encrypting files in {folder_path} ...\n')
                encrypt_file(filepath)


# decrypt a single file
def decrypt_file(filename):
    # read binary
    with open(filename, 'rb') as file:
        # is the file content not recognized?
        # is the key not recognized?
        data = file.read()
    decrypted_data = fernet.decrypt(data)
    # writes the decrypted content back into the file
    new_filename = filename.replace('.enc', '.xml')
    with open(new_filename, 'wb') as file:
        file.write(decrypted_data)
    os.remove(filename)


# decrypt the entire folder
def decrypt_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            filepath = os.path.join(root, file)
            if '.enc' in file:
                print(file)
                print(f'Decrypting files in {folder_path} ...\n')
                decrypt_file(filepath)


while True:
    try:
        encryptOrDecrypt = input(
            '[(e)ncrypt or (d)ecrypt]: ').lower()
        if encryptOrDecrypt == 'e':
            encrypt_folder(folderPath)
            print('Complete :)')
            break
        elif encryptOrDecrypt == 'd':
            decrypt_folder(folderPath)
            print('Complete :)')
            break
    except SyntaxError:
        print('Please enter a valid response')
