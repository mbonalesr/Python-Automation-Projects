import pandas as pd
import datetime as dt
import random
import smtplib

MY_EMAIL = "mau.python.bot@gmail.com"
PASSWORD = "buxe qqsc kgus mrai"

def generate_letter(name):
    """Chooses a random letter from folder and customises"""
    with open(f"letter-templates/letter_{random.randint(1,3)}.txt", mode="r") as letter_file:
        letter = letter_file.read()
        custom_letter = letter.replace("[NAME]", name)
        return custom_letter


def send_email(sender, password, recipient, message, birth_name):
    """Sends an email to a specific user"""
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(
            from_addr=sender,
            to_addrs=recipient,
            msg=f"Subject: Happy Birthday {birth_name}\nTo: {recipient}\n\n{message}".encode("utf-8")
    )


def main():
    """Checks today's date against the CSV file and triggers the letter generation and email process"""
    birthday_data = pd.read_csv("birthdays.csv")
    birth_dict = {(row['month'], row['day']): row for (index, row) in birthday_data.iterrows()}


    today = dt.datetime.now()
    today_month = today.month
    today_day = today.day


    if (today_month, today_day) in birth_dict:
        birthday_person = birth_dict[(today_month, today_day)]


        custom_letter = generate_letter(name=birthday_person['name'])

        send_email(sender=MY_EMAIL, password=PASSWORD, recipient=birthday_person['email'], 
                   message=custom_letter, birth_name=birthday_person['name'])
        

if __name__ == "__main__":
    main()
