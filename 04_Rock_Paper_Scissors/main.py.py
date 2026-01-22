import random, os
os.system('cls')

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors] #storing images

print("Welcome to the Rock-Paper-Scissors Game")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice == 0 or user_choice == 1 or user_choice == 2:
    print(game_images[user_choice]) #linking user choice with rps image
    
    print("Computer chose:")
    pc_choice = random.randint(0,len(game_images) - 1) 
    print(game_images[pc_choice]) #the same with the pc choice

    if user_choice == 0 and pc_choice == 2: #specific case -> rock vs scissors = rock wins
        print("Player wins!")
    elif user_choice == 2 and pc_choice == 0: #specific case -> scissors vs rock = rock wins
        print("Computer wins!")
    elif user_choice > pc_choice:
        print("Player wins!")
    elif user_choice < pc_choice:
        print("Computer wins!")
    else:
          print("It's a draw!") #same number match
else:
    print("Please choose a valid number!") #catch-all for invalid input
