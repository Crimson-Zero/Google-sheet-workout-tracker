import requests
from datetime import datetime

EXERCICE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = "https://api.sheety.co/SHEETY_API/SHEET_NAME/sheet1"

APP_ID = "EXERCISE_ID"
API_KEY = "EXERCISE_KEY"

headers = {
    "x-app-id" : APP_ID,
    "x-app-key":API_KEY,
    "Content-Type": "application/json"
    }


exercise = "Running for 7 mile and cycling 6 miles"

params = {
    
 "query":exercise,
 "gender":"gender",
 "weight_kg":weight,
 "height_cm":height,
 "age":age
}

response = requests.post(url=EXERCICE_ENDPOINT,json=params,headers=headers)

data = response.json()

headers = {
    "Authorization" : "Auth"
    }

exercises = data["exercises"]
current_date = datetime.now()
converted_date = current_date.strftime("%d/%m/%Y") 

converted_time = current_date.strftime("%X")



for exercise in exercises:
    
    exercise_name = exercise["name"]
    exercise_duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    sheet_params = {
        "sheet1": {
            "date": converted_date,
            "time" : converted_time,
            "exercise" : exercise_name.title(),
            "duration" : exercise_duration,
            "calories" : calories
            }

            }
    sheet_put = requests.post(url=SHEETY_ENDPOINT, json=sheet_params,headers=headers)
    print(sheet_put.raise_for_status())
    print(sheet_put.text)
    
    




