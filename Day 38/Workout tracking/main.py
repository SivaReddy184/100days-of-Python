import os
import requests
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

AUTH_USERNAME = os.environ["AUTH_USERNAME"]
AUTH_PASSWORD = os.environ["AUTH_PASSWORD"]
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

GENDER = "male"
WEIGHT_KG = 66
HEIGHT_CM = 170
AGE = 22

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/f675a0980916bc8e961bb4b42be69215/myWorkouts/workouts"
exercise_text = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

# ---------------------ADDING DATA IN SPREADSHEETS ------------------------------
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=(AUTH_USERNAME, AUTH_PASSWORD))

    print(sheet_response.text)




