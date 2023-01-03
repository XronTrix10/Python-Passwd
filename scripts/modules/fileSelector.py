import os
from modules import art


def filePath_Selector(main_path):

    files_path = main_path

    while True:

        print("Available OPTIONS: \n")
        print(
            "\t(1) Social Accounts\n\t(2) Email IDs\n\t(3) Websites\n\t(4) Apps\n\t(5) Others\n\t[6] Back"
        )

        while True:

            try:
                choice = int(input("\nYour choice: "))

            except ValueError:
                art.header()
                print("Wrong INPUT !!\n")
                print(
                    "\t(1) Social Accounts\n\t(2) Email IDs\n\t(3) Websites\n\t(4) Apps\n\t(5) Others\n\t[6] Back"
                )

            else:

                if choice < 1 or choice > 6:

                    art.header()
                    print(f"WRONG choice {os.environ.get('USERNAME')} ! Try again !\n")

                elif choice == 6:

                    art.header()
                    return main_path

                else:

                    if choice == 1:

                        files_path = os.path.join(main_path, "social")

                    elif choice == 2:

                        files_path = os.path.join(main_path, "emails")

                    elif choice == 3:

                        files_path = os.path.join(main_path, "websites")

                    elif choice == 4:

                        files_path = os.path.join(main_path, "apps")

                    elif choice == 5:

                        files_path = os.path.join(main_path, "others")

                    return files_path
