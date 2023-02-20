import os
from modules import art


"""
    This function displays the options of the avialable paths and returns the files path selected by the user. 
    main_path is used to later check from which path was the user came from and if they select back, they are taken back to the asked path. 
"""


def filePath_Selector(main_path):

    # assign main_path to files_path
    files_path = main_path

    while True:
        # print available options in orange and underlined with bold headings
        print(
            art.clr.orange,
            art.clr.underline,
            art.clr.bold,
            "AVAILABLE OPTIONS:",
            art.clr.reset,
        )
        # print accordingly pink colored options
        print(
            art.clr.pink,
            "\n\t(1) Social Accounts\n\t(2) Email IDs\n\t(3) Websites\n\t(4) Apps\n\t(5) Others\n\t[6] Back",
        )

        # loop untill a proper choice is made
        while True:

            try:
                # prompt for the choice
                print(art.clr.lightblue)
                choice = int(input("\nYour choice: "))

                # raise ValueError if the choice is not in range
                if choice < 1 or choice > 6:
                    raise ValueError

            # except valueError
            except ValueError:
                # display art header
                art.header()
                # display wrong choice message
                print(
                    art.clr.red,
                    f"WRONG choice {os.environ.get('USERNAME')} ! Try again !\n",
                )

                # display pink options
                print(
                    art.clr.pink,
                    "\n\t(1) Social Accounts\n\t(2) Email IDs\n\t(3) Websites\n\t(4) Apps\n\t(5) Others\n\t[6] Back",
                )

            else:

                # if choice is '6', return the main path
                if choice == 6:
                    art.header()
                    return main_path

                # else, if the choice is '1', return files_path of  Social Accounts
                elif choice == 1:
                    files_path = os.path.join(main_path, "social")

                # else, if the choice is 2, return files_path of Emails IDs
                elif choice == 2:

                    files_path = os.path.join(main_path, "emails")

                # else, if the choice is 3, return files_path of Websites
                elif choice == 3:

                    files_path = os.path.join(main_path, "websites")

                # else, if the choice is 4, return files_path of Apps
                elif choice == 4:

                    files_path = os.path.join(main_path, "apps")

                # else, if the choice is 5, return files_path of Others
                elif choice == 5:

                    files_path = os.path.join(main_path, "others")

                # return the respective files_path
                return files_path
