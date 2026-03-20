import os, random
os.system('cls')
from art import *
from game_data import *

score = 0

print(logo)

a_celebrity = random.choice(data)
b_celebrity = random.choice(data)


def format_celebrity(chosen):
    """Format celebrity data to give the user a clear idea"""
    return f"{chosen['name']}, a {chosen['description']}, from {chosen['country']}." # declare functions outside the loop


def comparing_followers(attempt, a_follows, b_follows):
        """Compares 'A' and 'B' followers based in the user's attempt, 
        returns True if the user guessed right or if there's a tie and 
        returns False if the user failed"""
        if (a_follows > b_follows and attempt == 'A') or (b_follows > a_follows and attempt == 'B'):
            return True
        elif a_follows == b_follows:
            return True
        else:
            return False


while True:

    print(f"Compare A: {format_celebrity(chosen=a_celebrity)}")
    print(versus)
    print(f"Against B: {format_celebrity(chosen=b_celebrity)}")

    guess = input("Who has more followers? Type 'A' or 'B':\t").upper()
    
    if guess not in ['A', 'B']:
        print("Please only type 'A' or 'B'!")
        continue

    a_followers = a_celebrity['follower_count']
    b_followers = b_celebrity['follower_count']
        
    result = comparing_followers(attempt=guess, a_follows=a_followers, b_follows=b_followers)
        
    if result == False:
        os.system('cls')
        print(f"Sorry, that's wrong. Final score: {score}")
        break
    elif result == True:
        score += 1
        print(f"You're right! Current score: {score}")
        a_celebrity = b_celebrity
        b_celebrity = random.choice(data)
