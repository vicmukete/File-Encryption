from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b'What i want to encrypt')
print(token)
clear = f.decrypt(token)
print(clear.decode())
