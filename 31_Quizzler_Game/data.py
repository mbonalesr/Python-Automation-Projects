import requests, os
os.system('cls')

params = {
    "amount":10,
    "type":"boolean"
}

try:
    response = requests.get("https://opentdb.com/api.php", params=params)
    response.raise_for_status()
    question_data = response.json()['results']
except requests.exceptions.ConnectionError: 
    print("No internet connection. Loading emergency questions...")
    question_data = [
        {
            "question": "An octopus has three hearts",
            "correct_answer": "True",
        }
    ]