import os
os.system('cls')

from art import logo

print(logo)

bids = {}

highest_bid = 0
name_winner = ""

auction = True

while auction:
    name = input("What is your name? ").title()
    bid = int(input("What is your bid? $"))

    bids[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if other_bidders == 'yes':
        os.system('cls') # clearing screen
    elif other_bidders == 'no':
        auction = False
    else:
        print("Invalid syntax, ending auction")
        break

os.system('cls')

for name, bid in bids.items(): # getting the winner of the auction
    if bid > highest_bid:
        highest_bid = bid
        name_winner = name
print(f"The winner is {name_winner} with a bid of ${highest_bid}")
