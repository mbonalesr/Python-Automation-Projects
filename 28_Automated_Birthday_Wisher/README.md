# Automated Birthday Wisher 🎂✉️

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)

## 📝 Description
The Automated Birthday Wisher is a Python script designed to check a database of birthdays daily and automatically send a customized, randomly selected birthday letter via email to anyone celebrating their special day.

The application features a seamless integration with Gmail's SMTP server and reads from a simple CSV database, making it easy to manage and maintain your contact list.

## ✨ Features
* **Daily Verification:** Uses the `datetime` module to check today's date against a saved `.csv` database.
* **Dynamic Templates:** Randomly selects between multiple `.txt` letter templates to keep the messages fresh and unique year after year.
* **Personalization:** Automatically parses the chosen template and replaces the placeholder `[NAME]` with the birthday person's actual name.
* **Automated Delivery:** Securely connects to the Gmail SMTP server using `smtplib` to deliver the email without manual intervention.


## 🛠️ Prerequisites
* Python 3.x
* Pandas library (`pip install pandas`)
* A Gmail account with **2-Step Verification** enabled and an **App Password** generated.

## 🚀 How to Use
1. Clone or download the repository to your local machine.
2. Open `main.py` and replace the placeholder credentials with your own (never share your App Password publicly!):
   ```python
   MY_EMAIL = "your.email@gmail.com"
   PASSWORD = "your_app_password_here"

## 🎓 Acknowledgements
This project was developed as part of a personalized learning journey to master Python automation, working with the `datetime` and `pandas` libraries, and integrating email services using the `smtplib` module.