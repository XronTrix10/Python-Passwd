from cryptography.fernet import Fernet
from os import path


key_path = path.expandvars(r'%APPDATA%\Python-Passwd-Data\locker.key')

def isKeyEmpty():
    # Creating file is doesn't exist
    f1 = open(key_path, 'w')
    f1.close

    with open(key_path, 'rb') as filekey:
        key = filekey.read()
        # checking if key is empty
        if len(key) == 0:
            keyGen()


# this function will be triggered onlly on first run
def keyGen():
    # key generation
    key = Fernet.generate_key()
    # string the key in a file
    with open(key_path, 'wb') as filekey:
        filekey.write(key)


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

    if mode == "encrypt":
        # encrypting the file
        changedFile = fernet.encrypt(original)
    elif mode == "decrypt":
        # decrypting the file
        changedFile = fernet.decrypt(original)

    #changing the original file
    with open(filePath, 'wb') as encrypted_file:
        encrypted_file.write(changedFile)
