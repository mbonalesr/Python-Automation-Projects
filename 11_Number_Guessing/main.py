import os, random
os.system('cls')
from art import logo

secret_number = random.randint(1,100)

EASY_LIVES = 10
HARD_LIVES = 5

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \t").lower()

def choosing_difficulty(difficulty):
    """Assigns the quantity of lives depending the level of the game"""
    if difficulty == 'easy':
        return EASY_LIVES
    elif difficulty == 'hard':
        return HARD_LIVES
    
turns = choosing_difficulty(difficulty)

game_over = False

def check_answer(attempt, number, lives):
    """Compares the user's guess with the secret number and displays messages for each scenario"""
    if attempt == number:
        print(f"You got it! The answer was {number}")
    elif attempt > number:
        lives -= 1
        print("Too high.\nGuess again!")
    elif attempt < number:
        lives -= 1
        print("Too low.\nGuess again!")
    return lives


while not game_over:
    print(f"You have {turns} attempts remaining to guess the number.")

    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        print("Please only type numbers!")
        continue

    if guess < 0 or guess > 100:
        print(f"{guess} is outside 1-100 limit, try another number!")
        continue

    turns = check_answer(attempt=guess, number=secret_number, lives=turns)

    if guess == secret_number:
        game_over = True

    if turns == 0:
        game_over = True
        print("You've run out of guesses. Refresh the page to run again.")
