import os, getpass, time
from os import path
from modules import art, endeCRYPT

main_path = path.expandvars(r"%APPDATA%\Python-Passwd-Data")
filePath = os.path.join(main_path, "pswd.key")


def authVault():

    success = False
    art.header()

    # checks if the user has already entered a password
    if os.path.exists(filePath):

        # decrypting the Vault password file
        for i in range(5):
            endeCRYPT.decode_file(filePath)

        # Loop for Password attempt
        for i in range(4):

            art.header()
            # asks the user to enter the password
            print(art.clr.red)
            password = getpass.getpass("Enter your VAULT Password: ")


            # opens the file 'pswd.key' in read mode to compare the password
            with open(filePath, "r") as f:

                # compares the password with the saved string
                if password == str(f.readline()):

                    art.header()
                    print(art.clr.green, "\nYou are Authenticated !", art.clr.reset, end='')
                    time.sleep(1.5)
                    art.header()
                    success = True
                    break

                else:

                    art.header()
                    print(art.clr.red, "\nWRONG key !")
                    print(art.clr.bold,f"\n{3-i} Attempts remaining !",art.clr.reset, end='')
                    time.sleep(1)

        # encrypting the Vault password file
        for i in range(5):
            endeCRYPT.encode_file(filePath)

        art.header()
        return success

    # will be executed only if the file 'pswd.key' doesn't exist
    else:

        while True:

            art.header()

            # asks the user to enter the password
            print(art.clr.red)
            password = getpass.getpass("Create your VAULT Password: ")
            password2 = getpass.getpass("Re-Enter VAULT Password: ")
            print(art.clr.reset)
            if password == password2:
                art.header()
                break
            else:
                print(art.clr.red,"\nPassword mismatch ! Please Try Again !")
                time.sleep(1)


        # opens the file 'pswd.key' in write mode to save the entered password
        with open(filePath, "w") as f:
            f.write(password)

        # encrypting the Vault password file
        for i in range(5):
            endeCRYPT.encode_file(filePath)

        return True
