import os
import requests
import smtplib
from dotenv import load_dotenv

load_dotenv()

MY_LAT = 19.705950
MY_LONG = -101.194984

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
email = os.environ.get("MY_EMAIL")
password = os.environ.get("PASSWORD")

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for weather in weather_data['list']:
    id = weather["weather"][0]['id']
    if id < 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr= email,
            to_addrs= "mau.botpython@yahoo.com",
            msg="Subject: It's going to rain today!\n\nRemember to bring an umbrella"
        )
    print("Status: Email sent successfully!")
else:
    print("Don't worry, it isn't raining!") 
