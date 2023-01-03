import os
from modules import art, pswdGen, endeCRYPT, fileEditor, fileManager, fileSelector
from os import path

main_path = path.expandvars(r"%APPDATA%\Python-Passwd-Data")


class ValueError_1(Exception):
    pass


def file_viewer(filePath):

    status = endeCRYPT.decode_file(filePath)

    if status != 1:
        print("\n" + "=" * 40)
        with open(filePath, "r") as file:

            for lines in file:
                print(lines, end="")
        print("\n\n" + "=" * 40)
    else:
        return 1

    endeCRYPT.encode_file(filePath)


def pswd_saver():

    art.header()

    while True:

        try:
            print("\nPlease SELECT or CREATE a file: ")
            print("\n\t(1) SELECT\n\t(2) CREATE")
            choice = int(input("\nYour choice: "))
            if choice < 0 or choice > 2:
                raise ValueError_1

        except ValueError:
            art.header()
            print("Wrong INPUT !!")

        except ValueError_1:
            art.header()
            print("Wrong CHOICE !!")

        else:

            if choice == 1:

                fileManager.fileManage(4)
                break

            elif choice == 2:

                files_path = fileSelector.filePath_Selector(main_path)

                if files_path == main_path:
                    return

                art.header()
                print(
                    "Now, give a name to your file. [ Example: Facebook, Instagram...etc ]\n"
                )
                header = input("Name: ")
                file_name = header + ".pswd"
                filePath = os.path.join(files_path, file_name)

                # creating the file
                with open(filePath, "w") as file:
                    file.write("\n\t\t[ " + header + " ]\n")

                endeCRYPT.encode_file(filePath)

                art.header()
                fileEditor.file_editor(filePath)
                break

            else:

                art.header()
                print("WRONG choice ! Try again !\n")


def main_fun():

    while True:

        try:

            print("AVAILABLE OPTIONS:\n")
            print(
                "\t(1) View saved passwords\n\t(2) Add a new credential\n\t(3) edit a File\n\t(4) Delete a File\n\t[5] Back"
            )

            choice = int(input("\nYour choice: "))

            if choice < 1 or choice > 5:
                raise ValueError_1

        except ValueError:
            art.header()
            print("Wrong INPUT !!\n")

        except ValueError_1:
            art.header()
            print("Wrong CHOICE !!\n")

        else:

            if choice == 1:

                art.header()
                print("AVAILABLE OPTIONS:\n")
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
                print("OPTIONS:\n")
                return
