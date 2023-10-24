import requests
import datetime
import os 

API_KEY = "0"
APP_KEY = "0"


header = {
    "x-app-id": APP_KEY,
    "x-app-key": API_KEY,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("Tell me which exercise you did today?: ")


post_params = {
    "query": exercise_input,
    "gender":"female",
    "weight_kg":47,
    "height_cm":169.64,
    "age":19
}

now = datetime.datetime.now()
response = (requests.post(url=exercise_endpoint, json=post_params, headers=header)).json()

exercise = response["exercises"][0]["user_input"]
duration = response["exercises"][0]["duration_min"]
calories = response["exercises"][0]["nf_calories"]

sheet_url = "https://api.sheety.co/0/cópiaDeMyWorkouts/workouts"

sheet_content = {
    "workout": {
        "date": now.strftime("%d/%m/20%y"),
        "time": now.strftime('%X'),
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories,
    }
}

sheet_header = {
    "Authorization": "Bearer rgaoiregaemrgemrlg454454k5l454gwg"
}

sheet_response = requests.post(sheet_url, json=sheet_content, headers=sheet_header)

print(sheet_response.text)