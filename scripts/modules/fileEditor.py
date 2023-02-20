import os
from modules import art, pswdGen, endeCRYPT, fileManager


# This function is used to modify credentials (login and password) from a given file.
def file_editor(filePath):

    # This is a custom exception used for input validation when the user makes a wrong choice.
    class ValueError_1(Exception):
        pass

    choice = 0

    # An infinite loop is being depicted which handles user choice.
    while True:

        try:

            print(
                art.clr.orange,
                art.clr.underline,
                art.clr.bold,
                "OPTIONS:",
                art.clr.reset,
            )
            print(
                art.clr.pink,
                "\n\t(1) Add an account\n\t(2) Edit existing credentials",
                art.clr.lightblue,
            )

            temp = int(input("\nEnter your choice: "))

            # This statement checks if the user entered an invalid choice.
            if temp < 1 or temp > 2:
                raise ValueError_1

        except ValueError:

            art.header()
            print(art.clr.red, "Wrong INPUT !!\n")

        # Raise the valueerror_1 custom exception when user enter an invalid choice.
        except ValueError_1:

            art.header()
            print(art.clr.red, "Wrong CHOICE !!\n")

        else:

            choice = temp
            break

    # If the user chooses to add an account, this statement executes the corresponding function.
    if choice == 1:
        add_account(filePath)

    # If the user chooses to edit existing credentials, it executes the corresponding code.
    elif choice == 2:

        art.header()

        # This statement decodes the file to update credentials.
        endeCRYPT.decode_file(filePath)

        with open(filePath, "r") as file:

            # read a list of lines into data
            data = file.readlines()

        while True:

            try:

                # Print Lines of file
                for i in range(len(data)):
                    print(art.clr.disable, f"({i}) {data[i]}", end="")

                print(
                    art.clr.reset,
                    art.clr.red,
                    "\n\nNow, Carefully enter the line number (shown on left) that you want to edit"
                    + "\n\nNOTE: That line MUST contain login, password or comment !!",
                    art.clr.lightblue,
                )

                line_no = int(input("\nEnter line number: "))

                # This statement checks if the user entered an invalid line number.
                if line_no < 0 or line_no > len(data):
                    raise ValueError
                
                elif data[line_no] == '\n':
                    raise ValueError_1

            except ValueError:

                art.header()
                print(art.clr.red, "Wrong INPUT !!\n", art.clr.reset)

            except ValueError_1:

                art.header()
                print(art.clr.red, "EMPTY Line Can't be Modified !!\n", art.clr.reset)

            else:

                break

        art.header()
        print(art.clr.lightblue, "\nNow Enter the new credential: \n")
        line = data[line_no].split()

        # This statement takes input from the user for the corresponding credential.
        credential = input(f"{line[0]} ")
        # This line stores the new credential in the appropriate line in the file.
        data[line_no] = line[0] + " " + credential + "\n"

        # and write everything back
        with open(filePath, "w") as file:
            file.writelines(data)

        # This statement encodes the file after the credentials have been updated.
        endeCRYPT.encode_file(filePath)

        art.header()
        print(art.clr.green, "File was successfully updated !", art.clr.cyan)

        input("\nPress ENTER to Continue...")
        art.header()
        return

    else:

        art.header()
        # This statement prints out an error message if the user enters an invalid choice.
        print(art.clr.red, f"WRONG choice {os.environ.get('USERNAME')} ! Try again !\n")
        # This statement calls the function again in order to give the user a chance to enter a valid choice.
        file_editor(filePath)


# Code to add an account
def add_account(filePath):

    """
    This function adds user accounts to the specified file.
    The account number, login, and password are required for the user to access the accounts. A comment can also be added.

    Parameters:
    filePath (string): Path to file where the user account is saved

    Returns:
    None
    """

    art.header()
    print(art.clr.lightblue)

    account_no = input("Enter the account number: ")
    
    art.header()
    print(art.clr.lightblue)

    login = input("Enter the login (email / mobile / username): ")

    art.header()

    pswd = ""

    # Handling Exception
    while True:

        try:

            print(
                art.clr.pink,
                "\n\t(1) Generate Password\n\t(2) Enter Password",
                art.clr.lightblue,
            )

            # Prompt user for choice
            choice_1 = int(input("\nEnter your Choice: "))

            # Verify that choice is valid
            if choice_1 < 1 or choice_1 > 2:
                raise ValueError

        except ValueError:
            art.header()
            print(art.clr.red, "Wrong CHOICE !!\n")

        else:
            if choice_1 == 1:
                # Generate password if choice is 1
                pswd = pswdGen.gen()
                break
            elif choice_1 == 2:
                # Prompt user to enter password if choice is 2
                art.header()
                print(art.clr.lightblue)
                pswd = input("Enter the password: ")
                break

    # Prompt user for comment
    art.header()
    print(art.clr.lightblue)
    comment = input("Enter Comment (Leave empty if not required): ")

    # Decode file
    endeCRYPT.decode_file(filePath)

    # Open file and add credentials
    with open(filePath, "a") as file:
        file.writelines(
            f"\n\n----** Acccount {account_no} **----"
            + f"\n\nlogin: {login}"
            + f"\nPassword: {pswd}"
            + f"\nComment: {comment}"
        )

    # Encode file
    endeCRYPT.encode_file(filePath)

    # Print success message
    art.header()
    print(art.clr.green, "Credentials were saved !", art.clr.reset)

    # Show the updated credentials
    fileManager.displayFile(filePath)
    
    print(art.clr.cyan)
    input("\nPress ENTER to Continue...")
    art.header()
