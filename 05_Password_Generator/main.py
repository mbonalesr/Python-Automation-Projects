import random,os
os.system('cls')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '/', '=', '?', '¿']

print('''
          _________________________________________________
         /                                                /|
        / _/_/_/_/_/ _/_/_/_/_/ _/_/_/_/ _/___/ _/_/_/_/ //
       /                                                //|
      / _/_/_/_/_/_/_/_/_/_/_/_/_/__/  _/_/_/ _/_/_/_/ //||
     / __/_/_/_/_/_/_/_/_/_/_/_/_/  / _/_/_/ _/_/_/_/ //_|/    ,---------
    /_/__/_/_/_/_/_/_/_/_/_/_/_/___/   _/   _/_/_/_/ //       /__/__/__/ /|
   / __/_/_/_/_/_/_/_/_/_/_/_/__/   _/_/_/ _/_/_/ / //       /          / |
  /   __/_________________/               ___/_/_/ //       /          /  .
 /                                                //       /          / .'
(________________________________________________(/       (__________(.'
      ''')
print("Welcome to Mau's Password Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("Now, how many numbers would you like?\n"))
nr_symbols = int(input("Finally, how many symbols would you like?\n"))

password = [] # empty password

for letter in range(0, nr_letters):
    password.append(random.choice(letters))

for number in range(0, nr_numbers):
    password.append(random.choice(numbers))

for symbol in range(0, nr_symbols):
    password.append(random.choice(symbols))

# print(password) # checking current password
random.shuffle(password)
# print(password) # new order password in screen

# final_password = "" # to convert list into string
# for character in password:
#     final_password += character # manual way

final_password = "".join(password) # easier way

print(f"Your password is: {final_password}")
