import os
from modules import art, pswdGen, endeCRYPT, pswdManager
from os import path

main_path = path.expandvars(r"%APPDATA%\Python-Passwd-Data")


def file_editor(filePath):
    class ValueError_1(Exception):
        pass

    choice = 0
    pswd = ""

    while True:
        try:
            print("OPTIONS: ")
            print("\n\t(1) Add an account\n\t(2) Edit existing credentials")
            temp = int(input("\nEnter your choice: "))

            if temp < 1 or temp > 2:
                raise ValueError_1
        except ValueError:
            art.header()
            print("Wrong CHOICE !!\n")
        except ValueError_1:
            art.header()
            print("Wrong INPUT !!\n")
        else:
            choice = temp
            break

    if choice == 1:

        art.header()
        account_no = input("Enter the account number: ")
        art.header()
        login = input("Enter the login (email / mobile / username): ")
        art.header()

        # Handling Exception
        while True:

            try:
                print("\n\t(1) Generate Password\n\t(2) Enter Password")
                choice_1 = int(input("\nEnter your Choice: "))
                if choice_1 < 1 or choice_1 > 2:
                    raise ValueError_1

            except ValueError:
                art.header()
                print("Wrong CHOICE !!\n")

            except ValueError_1:
                art.header()
                print("Wrong INPUT !!\n")

            else:
                if choice_1 == 1:
                    pswd = pswdGen.gen()
                elif choice_1 == 2:
                    pswd = input("Enter the password: ")

            art.header()
            comment = input("Enter Comment (Leave empty if not required): ")

            endeCRYPT.decode_file(filePath)

            with open(filePath, "a") as file:
                file.writelines(
                    f"\n\n----** Acccount {account_no} **----"
                    + f"\n\nlogin: {login}"
                    + f"\nPassword: {pswd}"
                    + f"\nComment: {comment}"
                )

            endeCRYPT.encode_file(filePath)

            art.header()
            print("Credentials were saved !")
            pswdManager.file_viewer(filePath)
            input("\nPress ENTER to Continue...")
            art.header()
            return

    elif choice == 2:

        art.header()

        endeCRYPT.decode_file(filePath)

        with open(filePath, "r") as file:
            # read a list of lines into data
            data = file.readlines()

        while True:

            try:
                # Print Lines of file
                for i in range(len(data)):
                    print(f"({i}) {data[i]}", end="")

                print(
                    "\n\nNow, Carefully enter the line number (shown on left) that you want to edit"
                    + "\n\nNOTE: That line MUST contain either login or password !!"
                )

                line_no = int(input("\nEnter line number: "))
                if line_no < 0 or line_no > len(data):
                    raise ValueError

            except ValueError:
                art.header()
                print("Wrong INPUT !!\n")
            else:
                break

        art.header()
        print("\nNow Enter the new credential: \n")
        line = data[line_no].split()

        credential = input(f"{line[0]} ")
        data[line_no] = line[0] + " " + credential + "\n"

        # and write everything back
        with open(filePath, "w") as file:
            file.writelines(data)

        endeCRYPT.encode_file(filePath)

        art.header()
        print("File was successfully updated !")

        input("\nPress ENTER to Continue...")
        art.header()
        print("OPTIONS: \n")
        return

    else:

        art.header()
        print(f"WRONG choice {os.environ.get('USERNAME')} ! Try again !\n")
        file_editor(filePath)
