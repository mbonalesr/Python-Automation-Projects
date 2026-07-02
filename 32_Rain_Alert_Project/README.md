# Rain Alert App 🌧️

An automated Python script that checks the weather forecast for the next few hours and sends an Email notification if rain is expected.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)
![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-EB6E4B?style=for-the-badge&logo=OpenWeatherMap&logoColor=white)

## 🚀 Features

- **Weather Forecasting**: Uses the OpenWeatherMap API to retrieve accurate forecast data 📊.
- **Automated Alerts**: Sends an Email notification using Python's built-in `smtplib` when rain is detected (weather ID < 700) 📧.
- **Security First**: Sensitive credentials (API keys, email addresses, and app passwords) are managed locally using environment variables and protected via `.gitignore` 🔐.

## 🎓 Acknowledgements

This project was developed as part of a personalized learning journey 
to master Python automation, working with external APIs using the 
`requests` library, sending automated email notifications via 
`smtplib`, and securing sensitive credentials locally with 
`python-dotenv`.

## 🛠️ Prerequisites

Before running the project, ensure you have Python installed and the required dependencies:

```bash
pip install requests python-dotenv