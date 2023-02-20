# Password Generator

import random, time
from modules import art

smlLtrs = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
capLtrs = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = [
    "!",
    "#",
    "$",
    "%",
    "&",
    "(",
    ")",
    "*",
    "+",
    "-",
    "_",
    "=",
    "`",
    "~",
    "<",
    ">",
    "?",
    ".",
    ",",
    ":",
    ";",
    "@",
    "/",
    "\\",
]

set = [smlLtrs, numbers, symbols, capLtrs]


def gen():

    """Generate a random password"""

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
        print(
            art.clr.lightblue,
            "\nYour Password: " + art.clr.green,
            final,
            art.clr.lightblue,
        )
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
    passwd += random.choice(symbols)

    for i in range(nr_letters - 4):
        chosen_set = random.choice(set)
        key = random.choice(chosen_set)
        passwd += key

    # Shuffling
    random.shuffle(passwd)

    # Converting to String
    final = ""
    for each in passwd:
        final += each

    # art.header()
    # print(art.clr.orange, "Generating: " + art.clr.green, f"{final}")

    return final
