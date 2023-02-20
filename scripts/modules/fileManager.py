import os
from modules import art, fileSelector, fileEditor, pswdManager, endeCRYPT
from os import path

# Path to the credential files
main_path = path.expandvars(r"%APPDATA%\Python-Passwd-Data")


class ValueError_1(Exception):
    pass


def fileManage(option):

    """
    This function is used to manage files in a directory.
    The argument option is used to indicate the action that needs to be carried out on the file."""

    art.header()
    # select the directory based on the password category
    files_path = fileSelector.filePath_Selector(main_path)

    # If the file path is equal to the default path, then the function will return.
    if files_path == main_path:
        return

    art.header()

    try:
        # The os.listdir fuction is used to get a list of files in the directory.
        list = os.listdir(files_path)

    # If the directory was not found, a FileNotFoundError is raised and a message is printed with probable causes.
    except FileNotFoundError:

        print(
            art.clr.red,
            "\nDirectory for the saved passwords was NOT FOUND !!\n\nProbable Causes :",
        )
        print(
            "\t(1) The Setup was UNSECCESSFULL !!\n\t(2) The Folder was accidentally MOVED or DELETED !!",
            art.clr.cyan,
        )
        input("\nPress ENTER to go back....")
        art.header()
        return

    else:

        # Checks if the folder is empty. If it is empty, a message is printed and the user is prompted to go back.
        if len(list) == 0:

            print(art.clr.purple, "\nNo Files here :^)", art.clr.cyan)
            input("\nPress ENTER to go back....")
            art.header()
            print(
                art.clr.orange,
                art.clr.underline,
                art.clr.bold,
                "OPTIONS:",
                art.clr.reset,
            )
            fileManage(option)

        else:

            # Defines the ValueError_1 custom exception.
            class ValueError_1(Exception):
                pass

            # This part of the code will loop until a valid selection is made by the user.
            # A menu is printed and the user is prompted with their choice.
            # If the input is invalid, a ValueError_1 is raised.

            while True:

                try:

                    for i in range(len(list)):
                        print(art.clr.pink, f"\t({i+1})", list[i].split(".")[0])

                    # If the user wants to enter another directory
                    print(f"\t[{len(list) + 1}] Back", art.clr.lightblue)

                    choice_1 = int(input("\nYour Choice: "))

                    if choice_1 < 1 or choice_1 > len(list) + 1:
                        raise ValueError_1

                except ValueError:
                    art.header()
                    print(art.clr.red, "Wrong INPUT !!\n")

                except ValueError_1:
                    art.header()
                    print(art.clr.red, "Wrong CHOICE !!\n")

                else:

                    # If the user wishes to go back, the function will return.
                    if choice_1 == len(list) + 1:

                        art.header()
                        return

                    # If the user makes a valid selection, the file path is built with os.path.join
                    # and the appropriate function is called depending on the value of the option argument.

                    else:

                        # join the path with user selected file name
                        filePath = os.path.join(files_path, list[choice_1 - 1])

                        if option == 1:
                            pswdViewer(filePath)
                            return

                        elif option == 2:
                            art.header()
                            fileEditor.file_editor(filePath)
                            return

                        elif option == 3:
                            file_deleter(filePath)
                            return


# This function helps to add account to files
def pswdAdder():

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

                fileManage(2)
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


# Define function to view passwords
def pswdViewer(filePath):

    art.header()

    # Checking for errors
    status = displayFile(filePath)

    # If no errors, prompt user to edit file
    if status != 1:
        print(art.clr.lightblue)
        choice_2 = input("\nDo you want to edit the file ? (Y/n): ").lower()

        # Prompt user to edit the file
        if choice_2 == "y":
            art.header()
            fileEditor.file_editor(filePath)
        # If user does not want to edit, return
        else:
            art.header()
            return


# This function is used to open a file and display its contents.
def displayFile(filePath):

    # If file is decrypted without error, then print the contents
    status = endeCRYPT.decode_file(filePath)

    if status != 1:

        print(art.clr.blue, "\n" + "=" * 60)

        with open(filePath, "r") as file:
            for lines in file:
                print(art.clr.green, lines, end="")

        print(art.clr.blue, "\n\n" + "=" * 60)

    else:
        return 1

    # Encrypt the file after viewing it to ensure security.
    endeCRYPT.encode_file(filePath)


# This function deletes the given file path permanently
def file_deleter(filePath):

    art.header()  # function to display header

    file_name = os.path.basename(filePath)  # get the file name from the file path
    file_name = os.path.splitext(file_name)[
        0
    ]  # split and extract file name without extension

    print(
        art.clr.red,  # set colour to red
        f"\nPermanently delete {file_name} ?" + art.clr.bold,
        " [ NOTE: This operation can't be undone ! ]",  # display warning
        art.clr.reset,
        art.clr.lightblue,  # set color to light blue
    )

    choice_2 = input(
        "\nYour decision: (Y/n): "
    ).lower()  # take input from user to decide if the file must be deleted

    # if the user chooses to delete the file
    if choice_2 == "y":

        art.header()
        print(
            art.clr.red, f"{file_name} was deleted forever !", art.clr.cyan
        )  # prints that the file has been deleted
        os.remove(filePath)  # removes file
        input("\nPress ENTER to Continue...")  # asks user to press enter to continue
        art.header()  # displays header

    # if user does not delete the file
    else:
        art.header()
        return
