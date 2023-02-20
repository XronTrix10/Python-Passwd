import os
from modules import (
    art,
    endeCRYPT,
    fileEditor,
    fileManager,
    fileSelector,
    MainPasswd,
)
from os import path

main_path = path.expandvars(r"%APPDATA%\Python-Passwd-Data")


class ValueError_1(Exception):
    pass


def accountAdder():

    art.header()

    while True:

        # Present user with two options - select or create
        try:
            print(
                art.clr.bold,
                art.clr.orange,
                "\nPlease SELECT a file or CREATE a new file: ",
                art.clr.reset,
            )
            print(art.clr.pink, "\n\t(1) SELECT\n\t(2) CREATE", art.clr.lightblue)
            choice = int(input("\nYour choice: "))

            if choice < 0 or choice > 2:  # ensuring the inputs are within range
                raise ValueError_1  

        except ValueError:  # Wrong input value
            art.header()
            print(art.clr.red, "Wrong INPUT !!\n")

        except ValueError_1:  # If input out of range
            art.header()
            print(art.clr.red, "Wrong CHOICE !!\n")

        else:

            art.header()
            
            if choice == 1:

                fileManager.fileManage(2)
                return

            elif choice == 2:

                # Select file path
                files_path = fileSelector.filePath_Selector(main_path)
                # If user cancels, return
                if files_path == main_path:
                    return

                art.header()

                # List any already existing files in the given path
                list = os.listdir(files_path)

                if len(list) != 0:

                    print(art.clr.blue, "\nAlready Present Files: \n")

                    for i in range(len(list)):

                        # Print only file names without extension
                        print(art.clr.pink, f"\t({i+1})", list[i].split(".")[0])

                # If no file is present
                else:
                    print(art.clr.green, "\nNo Files here, create one !")

                # Get the File Name
                print(
                    "\nNow, give a name to your file. [ Example: Facebook, Instagram...etc ]\n"
                    + art.clr.red,
                    "\nNOTE: Don't use name of already present file !\n",
                    art.clr.cyan,
                )
                header = input("Name: ")
                file_name = header + ".pswd"  # Create file name
                filePath = os.path.join(
                    files_path, file_name
                )  # Create full path to file

                # creating the file
                with open(filePath, "w") as file:
                    file.write("\n\t\t[ " + header + " ]\n")

                endeCRYPT.encode_file(filePath)  # Encrypt File

                art.header()

                # Redirecting to add account after creating the file
                fileEditor.add_account(filePath)
                break


def main_fun():

    """
    This function sets up the major options for the user.
    It provides them with an interactive interface where they can
    view saved passwords, add a new credential, edit and delete files.
    """

    # loop that continues until the user enters a valid option
    while True:

        # try loop to catch errors
        try:

            print(
                art.clr.orange,
                art.clr.underline,
                art.clr.bold,
                "AVAILABLE OPTIONS:",
                art.clr.reset,
            )  # print a list of the available options with number assigned
            print(
                art.clr.pink,
                "\n\t(1) View saved passwords\n\t(2) Add a new credential\n\t(3) Edit a File\n\t(4) Delete a File\n\t[5] Back",
                art.clr.lightblue,
            )

            choice = int(input("\nYour choice: "))  # prompt user for input

            if choice < 1 or choice > 5:  # ensuring the inputs are within range
                raise ValueError_1  # raise error if input out of range

        except ValueError:  # catch error if wrong input entered
            art.header()
            print(art.clr.red, "Wrong INPUT !!\n")

        except ValueError_1:  # catch error if wrong choice entered
            art.header()
            print(art.clr.red, "Wrong CHOICE !!\n")

        else:  # if valid input entered execute following code

            if choice == 1:  # displaying saved passwords

                art.header()
                print(
                    art.clr.orange,
                    art.clr.underline,
                    art.clr.bold,
                    "AVAILABLE OPTIONS:",
                    art.clr.reset,
                )

                fileManager.fileManage(1)

            elif choice == 2:  # adding a new credential

                art.header()
                accountAdder()

            elif choice == 3:  # editing a file

                art.header()
                fileManager.fileManage(2)

            elif choice == 4:  # deleting a file

                art.header()
                fileManager.fileManage(3)

            elif choice == 5:  # exit option

                art.header()
                print(
                    art.clr.orange,
                    art.clr.underline,
                    art.clr.bold,
                    "OPTIONS:",
                    art.clr.reset,
                )
                return  # return to the main screen


# Authentication function
def Authentication():

    if MainPasswd.authVault():
        main_fun()
    else:
        print(
            art.clr.orange,
            art.clr.underline,
            art.clr.bold,
            "OPTIONS:",
            art.clr.reset,
        )
        return
