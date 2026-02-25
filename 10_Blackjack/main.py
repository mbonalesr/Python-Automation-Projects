import os, random
os.system('cls')
from art import * # importing all variables

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Gives the user/PC a random card"""
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Returns the sum of all given cards """
    score = sum(cards)

    if score > 21 and 11 in cards: # ace conversion from 11 to 1
        score -= 10
        cards.remove(11)
        cards.append(1)
    return score


def blackjack_game():
    user_cards = []
    pc_cards = []

    for _ in range(0,2): # '_' means that we don't care about that variable and only want that Python repeats the loop 2 times
        user_cards.append(deal_card())
        pc_cards.append(deal_card())

    print(logo)

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        pc_score = calculate_score(pc_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")

        print(f"\nPC first card: {pc_cards[0]}")

        if pc_score == 21 or user_score >= 21: # checking if someone had already got a Blackjack or if someone went over 21
            game_over = True
            break

        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if another_card == 'y':
            user_cards.append(deal_card())
        elif another_card == 'n':
            user_score = calculate_score(user_cards)
            game_over = True

    if user_score <= 21:
        while pc_score < 17: # Dealer must draw to 16 and stand on all 17s
            pc_cards.append(deal_card())
            pc_score = calculate_score(pc_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"PC final hand: {pc_cards}, final score: {pc_score}")

    if user_score == pc_score:
        print("Push!")
        print(draw)
    elif pc_score == 21 and len(pc_cards) == 2:
        print("PC wins with a Blackjack!")
        print(lose)
    elif user_score == 21 and len(user_cards) == 2:
        print("You win with a Blackjack!")
        print(win)
    elif user_score > 21:
        print("You went over 21, PC wins!")
        print(lose)
    elif pc_score > 21:
        print("PC went over 21, you win!")
        print(win)
    elif user_score > pc_score:
        print(win)
    else:
        print("PC wins!")
        print(lose)

choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

while choice == 'y':
    os.system('cls')
    blackjack_game()

    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

print("Thanks for playing!")
