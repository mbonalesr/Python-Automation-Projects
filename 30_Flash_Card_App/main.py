from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
word = {}
to_learn = []

try:
    data = pd.read_csv('29_Flash_Card_App/data/words_to_learn.csv')
    
except FileNotFoundError:
    og_data = pd.read_csv('29_Flash_Card_App/data/cae_words.csv')
    to_learn = og_data.to_dict(orient='records')

else:
    to_learn = data.to_dict(orient='records')

def new_card():
    """Picks a random word from the list and displays it on the front card."""
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(to_learn)
    cae_word = word['word']

    canvas.itemconfig(title_label, text='Word', fill="black")
    canvas.itemconfig(word_label, text=cae_word, fill="black")
    canvas.itemconfig(card_backg, image=card_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Flips the card to show the English definition on the back."""
    definition = word['definition']

    canvas.itemconfig(title_label, text='Definition', fill="white")
    canvas.itemconfig(word_label, text=definition, fill="white")
    canvas.itemconfig(card_backg, image=back_card_img)

def mark_as_known():
    """Deletes known word from user list and saves progress"""
    to_learn.remove(word)
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv('29_Flash_Card_App/data/words_to_learn.csv', index=False)
    new_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Flashy - CAE Vocabulary')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)

card_img = PhotoImage(file='29_Flash_Card_App/images/card_front.png')
back_card_img = PhotoImage(file='29_Flash_Card_App/images/card_back.png')

card_backg = canvas.create_image(400, 263, image=card_img)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file='29_Flash_Card_App/images/right.png')
right_button = Button(image=right_img, highlightthickness=0, command=mark_as_known)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file='29_Flash_Card_App/images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_button.grid(column=0, row=1)

title_label = canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'))
word_label = canvas.create_text(400, 263, text='word', font=('Arial', 20, 'bold'))

new_card()

window.mainloop()
