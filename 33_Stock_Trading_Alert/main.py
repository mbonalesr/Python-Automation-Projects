import os
import requests
import smtplib
from dotenv import load_dotenv

load_dotenv()

STOCK = "CX" # Ticker symbol
COMPANY_NAME = "Cemex" # Company name for news search

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_key = os.environ.get("STOCK_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")

email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "CX",
    "apikey": stock_api_key,
}

news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": news_api_key
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"] # filtering dict

daily_data = [value for (key, value) in stock_data.items()]

yesterday_closing_price = daily_data[0]['4. close']

day_before_yesterday_closing_price = daily_data[1]['4. close']

if float(yesterday_closing_price) > float(day_before_yesterday_closing_price):
    symbol = "🔺"
else:
    symbol = "🔻"

difference = round(abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price)), 4)

diff_percent = round((difference / float(yesterday_closing_price)) * 100, 2)

if diff_percent <= 3:
    second_response = requests.get(NEWS_ENDPOINT, params=news_params)
    second_response.raise_for_status()
    news_data = second_response.json()["articles"]

    three_articles = news_data[:2]

    formatted_articles = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in three_articles]

    text_news = "\n".join(formatted_articles)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="mau.botpython@yahoo.com",
            msg=(f"Subject:{STOCK}: {symbol}{diff_percent}%\n\n{text_news}").encode("utf-8")
        )
    print(f"Status: Email sent successfully!")        
