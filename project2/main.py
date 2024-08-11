import random

number = int(random.uniform(1, 100))
a = -1
guesses = 0
while a != number:
    a = int(input("Guess a number between 1 and 100: "))
    if a < number:
        print("Too low! Try again.")
        guesses += 1
    elif a > number:
        print("Too high! Try again.")
        guesses += 1

print(f"Congratulations! You guessed the correct number {number} in {guesses} attempts.")