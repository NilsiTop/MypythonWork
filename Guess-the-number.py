"""
** Name: ** Guess-the-number.py**
** Created on ** 16 Januar 2019*
** Author: ** Nils Arne Topland*
"""

import random

print("This is random guess program where you type in any number between 0 - 100."
" You do have 5 tries to guess the random number from the computer.")

num = random.randint(0, 100)
MAX_TRIES = 5                                                 #antall forsøk til å gjette nummer
tries = 0
answer = "yes"


while tries < MAX_TRIES:
        try:
            guess = int(input("Guess a Number:"))
            tries += 1
            if guess == num:
                print("congratulations, you have guessed the right number,", num)
                print("Do you want to try again?")
                answer = input("Please type Yes to start guess")
                if answer == "yes":
                    continue

                elif answer == "no":
                    break

            elif guess > num:
                print("Close, but here is a hint DOWN!")

            elif guess < num:
                print("Close, but here is a hint UP!")

            if tries == 5:
                print("No more Tries. Do you want to ty again?")
                answer = input("type yes to try again")
                if answer == "yes":
                    continue
                if answer == "no":
                    break
        except ValueError:
            print("Please, use numbers")



