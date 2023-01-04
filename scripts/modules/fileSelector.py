import os
from modules import art


def filePath_Selector(main_path):

    files_path = main_path

    while True:

        print(
            art.clr.orange,
            art.clr.underline,
            art.clr.bold,
            "AVAILABLE OPTIONS:",
            art.clr.reset,
        )
        print(
            art.clr.pink,
            "\n\t(1) Social Accounts\n\t(2) Email IDs\n\t(3) Websites\n\t(4) Apps\n\t(5) Others\n\t[6] Back",
        )

        while True:

            try:
                print(art.clr.lightblue)
                choice = int(input("\nYour choice: "))

                if choice < 1 or choice > 6:
                    raise ValueError

            except ValueError:
                art.header()
                print(
                        art.clr.red,
                        f"WRONG choice {os.environ.get('USERNAME')} ! Try again !\n",
                    )
                print(
                    art.clr.pink,
                    "\n\t(1) Social Accounts\n\t(2) Email IDs\n\t(3) Websites\n\t(4) Apps\n\t(5) Others\n\t[6] Back",
                )

            else:

                if choice == 6:

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
