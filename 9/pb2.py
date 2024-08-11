import random

def game():
    print("Welcome to the Guessing Game!")
    score = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    print(f"Your score is {score}.")

    try:
        # Attempt to open the file and read the high score
        with open("./highscore.txt", "r") as f:
            highscore = f.read()
            if highscore:
                highscore = int(highscore)  # Convert to integer if there is content
            else:
                highscore = 0  # Default to 0 if file is empty
    except FileNotFoundError:
        highscore = 0  # Default to 0 if file does not exist

    print(f"Your high score is {highscore}.")

    # Update high score if the current score is higher
    if score > highscore:
        with open("./highscore.txt", "w") as f:
            f.write(str(score))
        print(f"New high score! {score}")

    return score

game()
