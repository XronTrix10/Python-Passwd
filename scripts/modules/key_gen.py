from cryptography.fernet import Fernet
from os import path

key_path = path.expandvars(r'%APPDATA%\Python-Passwd-Data\locker.key')

def keyGen():
    # key generation
    key = Fernet.generate_key()
    # string the key in a file
    with open(key_path, 'wb') as filekey:
        filekey.write(key)

keyGen()