from cryptography.fernet import Fernet
from os import path


key_path = path.expandvars(r'%APPDATA%\Python-Passwd-Data\locker.key')


def changeFile(filePath, mode):

    # opening the key
    with open(key_path, 'rb') as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)

    # opening the original file to encrypt
    with open(filePath, 'rb') as file:
        original = file.read()

    changedFile = original

    if mode == "encode":
        # encrypting the file
        changedFile = fernet.encrypt(original)
    elif mode == "decode":
        # decrypting the file
        changedFile = fernet.decrypt(original)

    #changing the original file
    with open(filePath, 'wb') as encrypted_file:
        encrypted_file.write(changedFile)
