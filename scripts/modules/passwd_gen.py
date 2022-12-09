# Password Generator 

import random
from modules import art

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&',
           '(', ')', '*', '+', '-', '_', '=', '`', '~', '<', '>', '?', '.', ',', ':', ';', "'", '"']

set = [letters, numbers, symbols]


def gen():

    choice = 'y'
    while choice == 'y':

        art.header()

        nr_letters = 0
        while nr_letters < 8:
            nr_letters = int(
                input("Length of the password you would like: "))
            if nr_letters < 8:
                art.header()
                print("Length is too short !! Try at least 8\n")

        passwd = ""

        for i in range(nr_letters):
            chosen_set = random.choice(set)
            key = random.choice(chosen_set)
            passwd += key

        art.header()
        print("You got: ", passwd)

        choice = input("\nRegenerate password ? (Y/n): ").lower()
        if choice != 'y':
            return passwd

