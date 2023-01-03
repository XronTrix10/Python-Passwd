import os
from modules import art, pswdGen, pswdManager


art.header()
print(f"What you upto {os.environ.get('USERNAME')} ?\n")

# Handling Proper Choice
while True:

    # Handling ValueError Exception
    while True:

        try:
            print("\t(1) Generate a password\n\t(2) Manage your passwords\n\t[3] Exit")
            choice_1 = int(input("\nEnter your choice: "))
        except ValueError:
            art.header()
            print("Please enter Proper Choice !\n")
        else:
            break

    if choice_1 == 1:

        new_paswd = pswdGen.gen()

        art.header()
        print(
            f"Your Password is: {new_paswd}\n"
            + "\nNOTE: Copy the password for future use !"
        )

        input("\nPress ENTER to Continue...")
        art.header()
        print("OPTIONS:\n")

    elif choice_1 == 2:

        art.header()
        pswdManager.main_fun()

    elif choice_1 == 3:

        os.system("cls")
        print(art.bye)
        break

    else:

        art.header()
        print(f"WRONG choice {os.environ.get('USERNAME')} ! Try again !\n")
