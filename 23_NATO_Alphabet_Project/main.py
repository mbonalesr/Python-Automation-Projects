import pandas
from art import logo

print(logo)

nato_phonetic_df = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row['letter']:row['code'] for (index, row) in nato_phonetic_df.iterrows()}

def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        nato_word = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_word)

generate_phonetic()