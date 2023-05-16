from art import logo
import random
import os

EASY_LEVELS = 10
HARD_LEVELS = 5


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()

    if difficulty == "easy":
        return EASY_LEVELS
    else:
        return HARD_LEVELS


# Clear terminal
os.system("cls")

# Print the logo
print(logo)

print("Welcome to the Number Guessing Game!")

print("I'm guessing of a number between 1 to 100.")
guessed_number = random.randint(1, 101)

guesses_left = set_difficulty()


is_over = False

while guesses_left > 0 and not is_over:
    print(f"You have {guesses_left} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))

    if user_guess > guessed_number:
        print("Too high.\nGuess again.")
        guesses_left -= 1
    elif user_guess < guessed_number:
        print("Too low.\nGuess again.")
        guesses_left -= 1
    else:
        print(f"You got it! The answer was {guessed_number}")
        is_over = True

if guesses_left == 0:
    print(f"You've run out of attempts.The number was {guessed_number} \nYou lose!")
