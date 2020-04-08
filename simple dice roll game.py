import math
import random

while True:
    print("I am going to roll a 6-sided dice.\nCan you guess what number it will be?")
    print("Enter a number between 1 and 6.\n")
    dice_roll = random.randint(1, 6)
    user_input = int(input("Enter your guess: "))

    if user_input == dice_roll:
        print("\nWow, lucky! You guessed it!\n\nI rolled a " + str(dice_roll) + "!")
    else:
        print("Nope! You guessed wrong!\n\nI rolled a " + str(dice_roll) + ".")

    if input("\nPlay again? Type \"yes\" or \"no\".") == "no":
        print("\n\n\nThank you for playing.\n")
        break
