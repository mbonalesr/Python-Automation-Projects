# 🪙 Automatic Bitcoin Price Monitor

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![API](https://img.shields.io/badge/API-CoinGecko-brightgreen?style=for-the-badge)

An automated Python script that continuously tracks the live price of Bitcoin, logs the data historically into a CSV file, and sends real-time email alerts when the price drops below a specific target.

## 🚀 Features

* **Real-Time Data:** Fetches live Bitcoin prices in USD using the free [CoinGecko API](https://www.coingecko.com/en/api).
* **Automated Data Logging:** Uses Pandas to seamlessly append timestamps and prices to a `.csv` file without overwriting existing history.
* **Smart Alerts:** Automatically sends an email notification via SMTP when the Bitcoin price falls to or below your defined target price.
* **Continuous Monitoring:** Runs perpetually with a 60-second delay between queries to avoid API rate limits.

## 📂 Data Output Format

The generated `bitcoin_historial.csv` will look like this:

| date       | hour     | price-usd |
|------------|----------|-----------|
| 2026-05-28 | 15-00-00 | 68450     |
| 2026-05-28 | 15-01-00 | 68430     |
| 2026-05-28 | 15-02-00 | 68455     |

## ⚙️ Configuration

Open the script and update the constants at the top of the file to match your preferences:

1. **`MY_EMAIL`**: The email address that will send the alert.
2. **`PASSWORD`**: Your email's App Password (do not use your standard password). *If using Gmail, you must generate an App Password in your Google Account settings.*
3. **`ALERT_PRICE`**: The target Bitcoin price (in USD) that triggers the email notification.
4. **Target Email**: Update the `to_addrs` parameter inside the `send_email_alert` function to the email address where you want to receive the notifications.

> **⚠️ Security Warning:** Never hardcode your real email passwords in scripts that you plan to upload to public repositories. Consider using Environment Variables (`os.environ`) for better security.

## 🛠️ Prerequisites

Before running the script, make sure you have Python installed along with the following libraries:

```bash
pip install requests pandas