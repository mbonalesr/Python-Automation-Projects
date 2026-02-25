import os
os.system('cls')
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(original_text, shift_amount, direction):
    crypted_word = [] # storing values

    if direction == 'decode':
        shift_amount *= - 1 # inverting shift
        
    for letter in original_text:
        if letter in alphabet:
            actual_index = alphabet.index(letter)
            new_index = (actual_index + shift_amount) % 26 # to cycle alphabet values on list
            crypted_word.append(alphabet[new_index])
        else:
            crypted_word.append(letter) # numbers, symbols or spaces

    print(f"Here's the {direction}d result: {''.join(crypted_word)}")
    
should_continue = True # flag to keep encrypting/decrypting

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction != 'encode' and direction != 'decode':
        print("Please write the specific function!")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(original_text = text, shift_amount = shift, direction = direction)

    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if choice == 'no':
        should_continue = False
        print("See you soon!")
