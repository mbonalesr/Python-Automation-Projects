from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    """Creates a fully random password according to specific characters."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '/', '=', '?', '¿']


    password_list = []

    letter_list = [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    number_list = [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]
    symbol_list = [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Pulls all info and saves it into a txt file"""
    website = website_input.get()
    email_user = email_user_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email_user,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!!")
    else:
        try:
            with open('data.json', mode='r') as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open('data.json', mode='w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
    
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    """Extracts website text and check if matches the database"""
    website = website_input.get()

    try:
        with open('data.json', mode='r') as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found')

    else:
        if website in data:
            messagebox.showinfo(title=f'{website}', 
            message=f"Email: {data[website]['email']}\n Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title='Error', message=f"No details for the {website} website exists.") 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Mau's Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=500, height=500)
password_img = PhotoImage(file='password.png')
canvas.create_image(250, 250, image=password_img)
canvas.grid(column=0, row=0, columnspan=3)

# --- ROW 1 ---
website_label = Label(text="Website:", font=("Lexend", 12, "normal"))
website_label.grid(column=0, row=1, sticky='E')

website_input = Entry(width=21)
website_input.grid(column=1, row=1, sticky='W')
website_input.focus()

search_button = Button(text='Search', width=10, command=find_password)
search_button.grid(column=2, row= 1, sticky='W')

# --- ROW 2 ---
email_user_label = Label(text="Email/Username:", font=("Lexend", 12, "normal"))
email_user_label.grid(column=0, row=2, sticky='E')

email_user_input = Entry(width=38)
email_user_input.grid(column=1, row=2, columnspan=2, sticky='EW')
email_user_input.insert(0, "maubr@gmail.com")

# --- ROW 3 ---
password_label = Label(text="Password:", font=("Lexend", 12, "normal"))
password_label.grid(column=0, row=3, sticky='E')

password_input = Entry(width=21)
password_input.grid(column=1, row=3, columnspan=1, sticky='W')

generate_passw = Button(text='Generate Password', command=generate_password)
generate_passw.grid(column=2, row= 3, sticky='W')

# --- ROW 4 ---
add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='EW')


window.mainloop()
