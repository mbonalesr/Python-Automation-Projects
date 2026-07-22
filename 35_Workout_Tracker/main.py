import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

GENDER = "male"
AGE = 25
WEIGHT_KG = 71
HEIGHT_CM = 174

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

NUTRITION_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/7ca1cda9d08e8d7735b8cf6cfbe4ec47/mauWorkouts/hoja1"

now = datetime.now()
date_string = now.strftime("%d/%m/%Y")
hour_string = now.strftime("%H:%M:%S")

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

BEARER_HEADERS = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

workout_params = {
    "query": input("Tell me what exercises you did: "),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER
}

response = requests.post(url=NUTRITION_ENDPOINT, json=workout_params, headers=HEADERS)
response.raise_for_status()
exercise_data = response.json()

sheet_inputs = {
    "hoja1":{
        "date": date_string,
        "time": hour_string,
        "exercise": exercise_data['exercises'][0]['name'].capitalize(),
        "duration": exercise_data['exercises'][0]['duration_min'],
        "calories": exercise_data['exercises'][0]['nf_calories']
    }
}

sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=BEARER_HEADERS)
sheet_response.raise_for_status()
sheet_data = sheet_response.json()
print(sheet_data)