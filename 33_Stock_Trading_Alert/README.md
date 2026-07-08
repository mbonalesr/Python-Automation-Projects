# 📈 Stock Trading Alert Automation

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-005571?style=for-the-badge&logo=python&logoColor=white)
![Dotenv](https://img.shields.io/badge/Dotenv-ECD53F?style=for-the-badge&logo=dotenv&logoColor=black)
![APIs](https://img.shields.io/badge/REST_API-008080?style=for-the-badge&logo=json&logoColor=white)

A Python automation script that tracks daily stock prices and sends a customized email alert containing the latest relevant news whenever a significant price fluctuation is detected. 

This project demonstrates the integration of multiple REST APIs, secure credential management, data parsing, and automated email dispatching using UTF-8 encoding.

---

## ✨ Features

* **Real-time Stock Tracking:** Fetches daily stock closing prices using the [Alpha Vantage API](https://www.alphavantage.co/).
* **Mathematical Analysis:** Calculates the percentage difference between the closing prices of the last two consecutive trading days.
* **Automated News Fetching:** If the stock fluctuates beyond a set threshold (e.g., 3%), it triggers the [NewsAPI](https://newsapi.org/) to retrieve the top 3 most relevant news articles about the company.
* **Email Digest Alert:** Formats the headlines and briefs into a clean, readable text block and sends an automated email using Python's built-in `smtplib`.
* **Visual Indicators:** Uses UTF-8 encoding to include direction indicators (🔺 for gains, 🔻 for losses) directly in the email subject line.
* **Secure:** Uses `python-dotenv` to keep API keys and email credentials safely hidden.

---

## 🛠️ Technologies & Libraries

* **Python 3.x**
* `requests` (for API calls)
* `smtplib` (for SMTP email protocol)
* `os` & `python-dotenv` (for environment variable management)