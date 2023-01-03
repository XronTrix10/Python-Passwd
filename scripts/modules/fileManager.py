import os
from modules import art, fileSelector, fileEditor, pswdManager
from os import path

main_path = path.expandvars(r"%APPDATA%\Python-Passwd-Data")


def fileManage(para):

    art.header()
    files_path = fileSelector.filePath_Selector(main_path)

    if files_path == main_path:
        return

    art.header()

    try:
        list = os.listdir(files_path)

    # If the directory was not found
    except FileNotFoundError:
        print(
            "\nDirectory for the saved passwords was NOT FOUND !!\n\nProbable Causes :"
        )
        print(
            "\t(1) The Setup was UNSECCESSFULL !!\n\t(2) The Folder was accidentally MOVED or DELETED !!"
        )
        input("\nPress ENTER to go back....")
        art.header()
        return

    else:

        # Checking if the folder is empty
        if len(list) == 0:

            print("No Files here :^)")
            input("\nPress ENTER to go back....")
            art.header()
            print("OPTIONS:\n")
            fileManage(para)

        else:

            class ValueError_1(Exception):
                pass

            while True:

                try:

                    for i in range(len(list)):
                        print(f"\t({i+1})", list[i].split(".")[0])

                    # If the user wants to enter another directory
                    print(f"\t[{len(list) + 1}] Back")

                    choice_1 = int(input("\nYour Choice: "))

                    if choice_1 < 1 or choice_1 > len(list) + 1:
                        raise ValueError_1

                except ValueError:
                    art.header()
                    print("Wrong INPUT !!\n")

                except ValueError_1:
                    art.header()
                    print("Wrong CHOICE !!\n")

                else:
                    # if user wants to go back
                    if choice_1 == len(list) + 1:

                        art.header()
                        return

                    else:

                        filePath = os.path.join(files_path, list[choice_1 - 1])

                        if para == 1:
                            pswd_viewer(filePath)
                            return
                        elif para == 2:
                            pswd_editor(filePath)
                            return
                        elif para == 3:
                            file_deleter(filePath)
                            return
                        elif para == 4:
                            pswd_saver(filePath)
                            return


def pswd_viewer(filePath):

    art.header()

    # Checking for errors
    status = pswdManager.file_viewer(filePath)

    if status != 1:
        choice_2 = input("\nDo you want to edit the file ? (Y/n): ").lower()

        if choice_2 == "y":
            art.header()
            fileEditor.file_editor(filePath)
        else:
            art.header()
            return


def pswd_editor(filePath):

    art.header()
    fileEditor.file_editor(filePath)


def file_deleter(filePath):

    art.header()

    file_name = os.path.basename(filePath)
    file_name = os.path.splitext(file_name)[0]

    print(
        f"Permanently delete {file_name} ?" + "\nNOTE: This operation can't be undone !"
    )

    choice_2 = input("\nYour decision: (Y/n): ").lower()

    if choice_2 == "y":

        art.header()
        print(f"{file_name} was deleted forever !")
        os.remove(filePath)
        input("\nPress ENTER to Continue...")
        art.header()

    else:
        art.header()
        print("OPTIONS:\n")
        return


def pswd_saver(filePath):

    art.header()
    fileEditor.file_editor(filePath)
