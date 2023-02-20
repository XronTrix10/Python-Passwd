import os
from modules import art, pswdGen, pswdManager


art.header()
print(art.clr.cyan, f"What you upto {os.environ.get('USERNAME')} ?")

# Handling Proper Choice
while True:

    # Handling ValueError Exception
    while True:

        try:

            print(
                art.clr.pink,
                "\n\t(1) Generate a password\n\t(2) Manage your passwords\n\t[3] Exit",
                art.clr.lightblue,
            )
            choice_1 = int(input("\nEnter your choice: "))

        except ValueError:

            # Show custom error message and start loop again if user enters invalid input
            art.header()
            print(art.clr.red, "Please enter Proper Choice !")

        else:

            # If valid input, break out of loop
            break

    # Execute code based on user's choice
    if choice_1 == 1:

        # Generate password
        new_paswd = pswdGen.gen()

        art.header()
        # Inform user of new password
        print(
            art.clr.cyan,
            "\nYour Password is: " + art.clr.green,
            f"{new_paswd}\n" + art.clr.red,
            "\nNOTE: Copy the password for future use !",
            art.clr.cyan,
        )

        input("\nPress ENTER to Continue...")
        art.header()
        print(
            art.clr.orange,
            art.clr.underline,
            art.clr.bold,
            "OPTIONS:",
            art.clr.reset,
        )

    elif choice_1 == 2:

        # Enter password management
        art.header()
        pswdManager.Authentication()

    elif choice_1 == 3:

        # Exit program
        os.system("cls")
        print(art.clr.orange, art.clr.bold, art.bye, art.clr.reset)
        break

    else:

        # Show custom error message if user enters invalid input
        art.header()
        print(art.clr.red, f"WRONG choice {os.environ.get('USERNAME')} ! Try again !")
