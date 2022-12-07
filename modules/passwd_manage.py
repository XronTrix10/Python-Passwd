import os
from modules import art, passwd_gen

main_path = "f:\\Documents\\01_Everything\\password_manager\\data\\"


def filePath_selector(choice):

    files_path = main_path

    if choice == 1:

        files_path = os.path.join(main_path, 'social')

    elif choice == 2:

        files_path = os.path.join(main_path, 'emails')

    elif choice == 3:

        files_path = os.path.join(main_path, 'websites')

    elif choice == 4:

        files_path = os.path.join(main_path, 'apps')

    elif choice == 5:

        files_path = os.path.join(main_path, 'others')

    return files_path


def file_editor(filePath):

    print("OPTIONS: ")
    print("\n\t(1) Add an account\n\t(2) Edit the file")
    choice = int(input("\nEnter your choice: "))
    pswd = ""
    if choice == 1:

        art.header()
        account_no = int(input("Enter the account number: "))
        login = input("Enter the login (email / mobile / username): ")
        print("\n\t(1) Generate Password\n\t(2) Enter Password")
        choice_1 = int(input("\nEnter your Choice: "))
        if choice_1 == 1:
            pswd = passwd_gen.gen()
        elif choice_1 == 2:
            pswd = input("Enter the password: ")
        comment = input("Enter Comment (Leave empty if not required): ")
        with open(filePath, 'a') as file:
            file.writelines(
                f"\n\n----** Acccount {account_no} **----" + f"\n\nlogin: {login}" + f"\nPassword: {pswd}" + f"\nComment: {comment}")

        art.header()
        print("Credentials were saved !")
        file_viewer(filePath)
        input("\nPress ENTER to Continue...")
        art.header()
        print("OPTIONS: \n")
        return

    elif choice == 2:

        art.header()

        with open(filePath, 'r') as file:
            # read a list of lines into data
            data = file.readlines()

        # Print Lines of file
        for i in range(len(data)):
            print(f"({i}) {data[i]}", end="")

        print("\n\nNow, Carefully enter the line number (shown on left) that you want to edit" +
              "\nNOTE: That line should contain either login or password !!")
        line_no = int(input("\nEnter line number: "))

        art.header()
        print("\nNow Enter the new credential: \n")
        line = data[line_no].split()

        credential = input(f"{line[0]} ")
        data[line_no] = line[0] + " " + credential + "\n"

        # and write everything back
        with open(filePath, 'w') as file:
            file.writelines(data)

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


def file_viewer(filePath):

    print("\n" + "="*20 + "\n")
    with open(filePath, 'r') as file:

        for lines in file:
            print(lines, end="")
    print("\n\n" + "="*20)


def pswd_viewer():

    files_path = main_path

    print(
        "\t(1) Social Accounts\n\t(2) Email IDs\n\t(3) Websites\n\t(4) Apps\n\t(5) Others\n\t[6] Back")
    choice = int(input("\nYour choice: "))

    if choice < 1 or choice > 6:

        art.header()
        print(f"WRONG choice {os.environ.get('USERNAME')} ! Try again !\n")
        pswd_viewer()

    elif choice == 6:

        art.header()
        # print("OPTIONS:\n")
        return

    else:

        files_path = filePath_selector(choice)

    art.header()
    list = os.listdir(files_path)

    # Checking if the folder is empty
    if len(list) == 0:

        print("No Files here :^)")
        input("\nPress ENTER to go back....")
        art.header()
        print("OPTIONS:\n")
        pswd_viewer()

    else:

        for i in range(len(list)):
            print(f"\t({i+1})", list[i].split('.')[0])

        # If the user wants to enter another directory
        print(f"\t[{len(list) + 1}] Back")

        choice_1 = int(input("\nYour Choice: "))

        # if user wants to go back
        if choice_1 == len(list) + 1:

            art.header()
            pswd_viewer()

        else:

            filePath = os.path.join(files_path, list[choice_1 - 1])

            art.header()

            file_viewer(filePath)

            choice_2 = input("\nDo you want to edit it ? (Y/n): ").lower()

            if choice_2 == 'y':
                art.header()
                file_editor(filePath)
            else:
                art.header()
                print("OPTIONS:\n")
                return


def pswd_saver():

    files_path = main_path
    print("Select Category: ")
    print(
        "\n\t(1) Social Accounts\n\t(2) Email IDs\n\t(3) Websites\n\t(4) Apps\n\t(5) Others\n\t[6] Back")
    choice_1 = int(input("\nYour choice: "))

    if choice_1 < 1 or choice_1 > 6:

        art.header()
        print(f"WRONG choice {os.environ.get('USERNAME')} ! Try again !\n")
        pswd_saver()

    elif choice_1 == 6:

        art.header()
        # print("OPTIONS:\n")
        return

    else:

        files_path = filePath_selector(choice_1)

    art.header()
    print("Please SELECT or CREATE a file: ")
    print("\n\t(1) SELECT\n\t(2) CREATE")
    choice = int(input("\nYour choice: "))

    if choice == 1:

        art.header()
        list = os.listdir(files_path)

        # Checking if the folder is empty
        if len(list) == 0:

            print("No Files here :^)")
            input("\nPress ENTER to go back....")
            art.header()
            pswd_saver()

        else:

            for i in range(len(list)):
                print(f"\t({i+1})", list[i].split('.')[0])

             # If the user wants to enter another directory
            print(f"\t[{len(list) + 1}] Back")

            choice_1 = int(input("\nYour Choice: "))

            # if user wants to go back
            if choice_1 == len(list) + 1:

                art.header()
                pswd_saver()

            else:

                path_to_file = os.path.join(files_path, list[choice_1 - 1])
                art.header()
                file_editor(path_to_file)

    elif choice == 2:

        art.header()
        file_name = input("Enter the name of the file: ")
        file_name += ".pswd"
        path_to_file = os.path.join(files_path, file_name)
        f1 = open(path_to_file, 'w')
        f1.close
        art.header()
        file_editor(path_to_file)

    else:

        art.header()
        print("WRONG choice ! Try again !\n")
        pswd_saver()


def main_fun():

    while True:

        choice = 0

        print("AVAILABLE OPTIONS:\n")
        print(
            "\t(1) View saved passwords\n\t(2) Create a new credential\n\t[3] Back")
        choice = int(input("\nYour choice: "))

        if choice == 1:

            art.header()
            print("AVAILABLE OPTIONS:\n")
            pswd_viewer()

        elif choice == 2:

            art.header()
            pswd_saver()

        elif choice == 3:

            art.header()
            print("OPTIONS:\n")
            return

        else:
            art.header()
            print("WRONG choice ! Try again !\n")
            main_fun()
