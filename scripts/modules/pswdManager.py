from modules import (
    art,
    fileManager,
    fileManager,
    MainPasswd,
)
from os import path

main_path = path.expandvars(r"%APPDATA%\Python-Passwd-Data")


class ValueError_1(Exception):
    pass



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
                "\n\t(1) View saved passwords\n\t(2) Add a new credential\n\t(3) edit a File\n\t(4) Delete a File\n\t[5] Back",
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
                fileManager.pswdAdder()

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
