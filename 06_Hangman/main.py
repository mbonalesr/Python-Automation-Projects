import random, os
from hangman_art import logo, stages
from hangman_words import word_list
os.system('cls')

lives = 0

print(logo)

chosen_word = random.choice(word_list)
# print(chosen_word) # view word with aligned with placeholder

placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)

display = list(placeholder) # indexing and comparing

end_of_game = False

guessed_letter = []

while not end_of_game:
    print(f"************<??>/{6-lives} Lives Left************")
    guess = input("Guess a letter: ").lower()

    if guess not in guessed_letter:
        #print(display) # check index of secret word
        guessed_letter.append(guess) #avoid repetition

        for index in range(len(chosen_word)):
            if guess == chosen_word[index]:
                display[index] = guess
        
        if guess not in chosen_word:
            lives += 1
            print(f"You guessed {guess}, that'not in the word. You lose a life!")

            # print(lives)
        if lives == 6:
                end_of_game = True
                print(f"*********You Lose!**********\nThe secret word was: {chosen_word}")
        elif "_" not in display:
                end_of_game = True
                print("**********You Win!**********")

        # display = "".join(display)
        # print(display)

        # Correct way
        print("".join(display)) # avoid convert in string and only show progress

        print(stages[lives])
    else:    
        print(f"You have already entered letter {guess}!")
