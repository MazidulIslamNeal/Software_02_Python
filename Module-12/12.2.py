import json
import requests

city = input("Please enter the name of the city you want to check: ")
api_key = "a434474b1454398de0692cf26d48b80a"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    if response.status_code == 200:
        json_response = response.json()
        temp = json_response["main"]["temp"]
        description = json_response["weather"][0]["description"]
        print(f"Current weather in the city {city.capitalize()} is: {temp}°C with {description}.")
except requests.exceptions.RequestException as e:
    print("We encountered an error. Try again.")
