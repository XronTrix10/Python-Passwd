# Password Generator

import random, time
from modules import art
import string


smlLtrs = string.ascii_lowercase
capLtrs = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

set = [smlLtrs, numbers, symbols, capLtrs]


def gen():

    art.header()
    nr_letters = 0

    # Check if password is 8 or more letters, if not ask for correct number of letters
    while nr_letters < 8:
        try:
            print(art.clr.lightblue)
            nr_letters = int(input("Length of the password you would like: "))
        except ValueError:
            art.header()
            print(art.clr.red, "Wrong INPUT !!\n")
        else:
            if nr_letters < 8:
                art.header()
                print(art.clr.red, "Length is too short !! Try at least 8\n")

    choice = "y"

    # Continuously generate a new password until user inputs 'n'
    while choice == "y":
        # Generate a new password
        final = Gen_paswd(nr_letters)
        # Cool Loading bar
        art.header()
        print(art.clr.yellow, "\nGenerating strong password....\n", art.clr.green)
        for i in range(20):
            print("█" * (i + 1) + "▓" * (20 - i - 1) + f" {(i+1)*5}%", end="\r")
            time.sleep(0.09)

        art.header()
        print(art.clr.green, "\nYour Password: ", final, art.clr.lightblue)
        print(
            art.clr.red,
            f"\nTime to crack the password is approx {random.randint(2,4)} years and {random.randint(2,11)} months !",
            art.clr.lightblue,
        )

        choice = input("\nRegenerate password ? (Y/n): ").lower()

        # Return Final Password
        if choice != "y":
            return final


def Gen_paswd(nr_letters):

    passwd = []
    # Making sure the generated password has all types of chars
    passwd += random.choice(smlLtrs)
    passwd += random.choice(capLtrs)
    passwd += random.choice(numbers)

    symbol_counter = 0

    while symbol_counter < 3:
        temp = random.choice(symbols)
        if temp not in passwd:
            passwd.append(temp)
            symbol_counter += 1

    for i in range(nr_letters - 6):
        chosen_set = random.choice(set)
        key = random.choice(chosen_set)
        passwd += key

    # Shuffling
    random.shuffle(passwd)

    # Converting to String
    final = ""
    for each in passwd:
        final += each


    return final
