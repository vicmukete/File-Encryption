from cryptography.fernet import Fernet
import os

folderPath = r'C:\Users\muket\Desktop\Projects\Unethical\WiFi PWs'

# Saves the encryption/decryption key
key_path = r'C:\Users\muket\Desktop\Real Projects\File Encryption\key.txt'

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
    print(fernet, '\n')
    encrypted_data = fernet.encrypt(data)
    print(encrypted_data)

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
                print(f'Encrypting files in {folder_path} ...')
                encrypt_file(filepath)


# decrypt a single file
def decrypt_file(filename):
    # read binary
    with open(filename, 'rb') as file:
        # is the file content not recognized?
        # is the key not recognized?
        data = file.read()
    print(fernet)
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
                print(f'Decrypting files in {folder_path} ...')
                print(file)
                decrypt_file(filepath)

decrypt_folder(folderPath)


'''while True:
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
'''
