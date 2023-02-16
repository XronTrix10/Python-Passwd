import os
from modules import art, pswdGen, pswdManager


art.header()
print(art.clr.cyan, f"\nWhat you upto {os.getlogin()} ?")

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
            art.header()
            print(art.clr.red, "Please enter Proper Choice !")
        else:
            break

    if choice_1 == 1:

        new_paswd = pswdGen.gen()

        art.header()
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

        art.header()
        pswdManager.Authentication()

    elif choice_1 == 3:

        os.system("clear")
        print(art.clr.orange, art.clr.bold, art.bye, art.clr.reset)
        break

    else:

        art.header()
        print(
            art.clr.red, f"WRONG choice {os.environ.get('USERNAME')} ! Try again !"
        )
