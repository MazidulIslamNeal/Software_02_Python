import json
import requests

# Random Chuck Norris Jokes

response = "https://api.chucknorris.io/jokes/random"
joke = requests.get(response)
json_data = joke.json()
print(json_data["value"])
