'''
1 for snake
-1 for water
0 for gun


'''

import random

# Ensure random.choice works with the correct list
choices = ["snake", "water", "gun"]
computer_choice = random.choice(choices)
youstr = input("Enter your choice (snake, water, gun): ").strip().lower()

# Check if user input is valid
if youstr not in choices:
    print("Invalid input! Please enter snake, water, or gun.")
else:
    yourDict = {"snake": 1, "water": -1, "gun": 0}
    you = yourDict[youstr]
    reversedDict = {1: "snake", -1: "water", 0: "gun"}
    computer = yourDict[computer_choice]

    print(f"You chose {reversedDict[you]} and the computer chose {reversedDict[computer]}")

    if computer == you:
        print("It's a tie!")
    else:
        if (computer == 1 and you == -1): 
            print("You lose!")
        elif (computer == 1 and you == 0):
            print("You win!")
        elif (computer == -1 and you == 1):
            print("You win!")
        elif (computer == -1 and you == 0):
            print("You lose!")
        elif (computer == 0 and you == 1):
            print("You lose!")
        elif (computer == 0 and you == -1):
            print("You win!")
