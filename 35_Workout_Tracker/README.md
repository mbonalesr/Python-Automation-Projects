# 💪📈 NLP Workout Tracker Module

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-005571?style=for-the-badge&logo=python&logoColor=white)
![Dotenv](https://img.shields.io/badge/Dotenv-ECD53F?style=for-the-badge&logo=dotenv&logoColor=black)
![APIs](https://img.shields.io/badge/REST_API-008080?style=for-the-badge&logo=json&logoColor=white)

A Python module that interacts with the Nutritionix and Sheety APIs to track daily workouts and log them into a Google Spreadsheet. Just type what you did in plain English, and the script will calculate the calories and log the data using standard HTTP requests.

This project demonstrates the use of REST API methods (`POST`), Natural Language Processing, header authentication (Bearer Tokens), date formatting, and secure environment variable management.

---

## ✨ Features

* **Natural Language Processing:** Uses the Nutritionix API to understand plain text exercise descriptions and accurately calculate calories burned.
* **Data Entry (POST):** Add new daily rows dynamically using `datetime` to log your habits directly into Google Sheets.
* **Time Tracking:** Automatically captures and logs the exact date and time of the workout entry.
* **Secure Configurations:** Uses `python-dotenv` to keep the API tokens safely hidden, utilizing custom variables to prevent OS environment clashes.

---

## 🛠️ Technologies & Libraries[cite: 1]

* **Python 3.x**
* `requests` (for handling HTTP `POST` requests)
* `datetime` (for dynamic date formatting and targeting specific records)
* `os` & `python-dotenv` (for secure environment variable extraction)

---

## 🎓 Acknowledgements
This project was developed as part of a personalized learning journey to master interacting with REST APIs, handling POST requests, and securely managing environment variables in Python.
* Inspired by the [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu.
* Exercise NLP powered by the [Nutritionix API](https://www.nutritionix.com/business/api).
* Google Sheets integration made possible by [Sheety](https://sheety.co/).