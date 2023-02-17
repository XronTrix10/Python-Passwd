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


def file_viewer(filePath):

    status = endeCRYPT.decode_file(filePath)

    if status != 1:
        print(art.clr.blue, "\n" + "=" * 60)

        with open(filePath, "r") as file:
            for lines in file:
                print(art.clr.green, lines, end="")

        print(art.clr.blue, "\n\n" + "=" * 60)
    else:
        return 1

    endeCRYPT.encode_file(filePath)


def pswd_saver():

    art.header()

    while True:

        try:
            print(
                art.clr.bold,
                art.clr.orange,
                "\nPlease SELECT a file or CREATE a new file: ",
                art.clr.reset,
            )
            print(art.clr.pink, "\n\t(1) SELECT\n\t(2) CREATE", art.clr.lightblue)
            choice = int(input("\nYour choice: "))
            if choice < 0 or choice > 2:
                raise ValueError_1

        except ValueError:
            art.header()
            print(art.clr.red, "Wrong INPUT !!\n")

        except ValueError_1:
            art.header()
            print(art.clr.red, "Wrong CHOICE !!\n")

        else:

            art.header()
            if choice == 1:

                fileManager.fileManage(2)
                return

            elif choice == 2:

                files_path = fileSelector.filePath_Selector(main_path)

                if files_path == main_path:
                    return

                art.header()

                # Listing The present files
                list = os.listdir(files_path)
                if len(list) != 0:
                    print(art.clr.blue, "\nAlready Present Files: \n")
                    for i in range(len(list)):
                        print(art.clr.pink, f"\t({i+1})", list[i].split(".")[0])
                else:
                    print(art.clr.green, "\nNo Files here, create one !")

                print(
                    "\nNow, give a name to your file. [ Example: Facebook, Instagram...etc ]\n"
                    + art.clr.red,
                    "\nNOTE: Don't use name of already present file !\n",
                    art.clr.cyan,
                )
                header = input("Name: ")
                file_name = header + ".pswd"
                filePath = os.path.join(files_path, file_name)

                # creating the file
                with open(filePath, "w") as file:
                    file.write("\n\t\t[ " + header + " ]\n")

                endeCRYPT.encode_file(filePath)

                art.header()
                fileEditor.add_account(filePath)
                break


def main_fun():

    while True:

        try:

            print(
                art.clr.orange,
                art.clr.underline,
                art.clr.bold,
                "AVAILABLE OPTIONS:",
                art.clr.reset,
            )
            print(
                art.clr.pink,
                "\n\t(1) View saved passwords\n\t(2) Add a new credential\n\t(3) edit a File\n\t(4) Delete a File\n\t[5] Back",
                art.clr.lightblue,
            )

            choice = int(input("\nYour choice: "))

            if choice < 1 or choice > 5:
                raise ValueError_1

        except ValueError:
            art.header()
            print(art.clr.red, "Wrong INPUT !!\n")

        except ValueError_1:
            art.header()
            print(art.clr.red, "Wrong CHOICE !!\n")

        else:

            if choice == 1:

                art.header()
                print(
                    art.clr.orange,
                    art.clr.underline,
                    art.clr.bold,
                    "AVAILABLE OPTIONS:",
                    art.clr.reset,
                )
                fileManager.fileManage(1)

            elif choice == 2:

                art.header()
                pswd_saver()

            elif choice == 3:

                art.header()
                fileManager.fileManage(2)

            elif choice == 4:

                art.header()
                fileManager.fileManage(3)

            elif choice == 5:

                art.header()
                print(
                    art.clr.orange,
                    art.clr.underline,
                    art.clr.bold,
                    "OPTIONS:",
                    art.clr.reset,
                )
                return


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
