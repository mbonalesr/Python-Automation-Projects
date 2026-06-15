import os
import requests
import time
import smtplib
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# ---------------------------- CONSTANTS ------------------------------- #
CSV_PATH = "29_Automatic_Bitcoin_Monitor/bitcoin_historial.csv"
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")
ALERT_PRICE = 76000

def obtain_bitcoin_price():
    """Queries the CoinGecko API and returns the current price of Bitcoin"""
    my_params = {
        "ids": "bitcoin",
        "vs_currencies":"usd",
    }
    response = requests.get("https://api.coingecko.com/api/v3/simple/price", params=my_params)
    response.raise_for_status()
    data = response.json()

    return data["bitcoin"]["usd"]


def save_to_history(price, date, hour):
    """It creates a DataFrame with the new record and appends it to the CSV file."""
    new_register = {
        "date": [date],
        "hour": [hour],
        "price-usd": [price],
    }
    register = pd.DataFrame(new_register)

    try:
        existing_record = pd.read_csv(CSV_PATH)
        updated_record = pd.concat([existing_record, register])
        updated_record.to_csv(CSV_PATH, index=False) 
    except FileNotFoundError:
        register.to_csv(CSV_PATH, index=False)


def send_email_alert(price, hour):
    """It connects to the SMTP server and sends the alert notification."""
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr= MY_EMAIL,
            to_addrs= "mau.botpython@yahoo.com",
            msg=f"Subject: Bitcoin Price Lower!\n\n{hour} Successful consultation. Current price: ${price}"
    )
    print(f"[{hour}] Buy alert sent! Current price: ${price}")

# ---------------------------- MAIN CYCLE ------------------------------- #

while True:
    try:
        bitcoin_price = obtain_bitcoin_price()
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_hour = now.strftime("%H-%M-%S")

        save_to_history(bitcoin_price, current_date, current_hour)

        if bitcoin_price <= ALERT_PRICE:
            send_email_alert(bitcoin_price, current_hour)

    except Exception as e:
        print(f"Unexpected error: {e}")
        
    time.sleep(60)
