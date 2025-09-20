import requests
import json

# Common headers (API key + host)
headers = {
    "x-rapidapi-key": "b21697a4f3mshc18a3118f1a2e72p142c1bjsn2433e369a8a8",
    "x-rapidapi-host": "open-weather13.p.rapidapi.com"
}

# 1. Weather by City
url_city = "https://open-weather13.p.rapidapi.com/city"
query_city = {"city": "new york", "lang": "EN"}
response_city = requests.get(url_city, headers=headers, params=query_city)
print("=== Weather by City ===")
print(json.dumps(response_city.json(), indent=4))

# 2. Weather by Latitude/Longitude
url_latlon = "https://open-weather13.p.rapidapi.com/latlon"
query_latlon = {"latitude": "40.730610", "longitude": "-73.935242", "lang": "EN"}
response_latlon = requests.get(url_latlon, headers=headers, params=query_latlon)
print("\n=== Weather by Latitude/Longitude ===")
print(json.dumps(response_latlon.json(), indent=4))

# 3. 5-Day Forecast
url_forecast = "https://open-weather13.p.rapidapi.com/fivedaysforcast"
query_forecast = {"latitude": "40.730610", "longitude": "-73.935242", "lang": "EN"}
response_forecast = requests.get(url_forecast, headers=headers, params=query_forecast)
print("\n=== 5-Day Forecast ===")
print(json.dumps(response_forecast.json(), indent=4))