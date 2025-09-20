import requests

BASE_URL = "https://apiexample-d0f4.onrender.com"

# Add API
add_params = {"x": "5", "y": "5"}
add_response = requests.get(f"{BASE_URL}/add", params=add_params)

print("Add Response:", add_response.json())

# Subtract API
subtract_params = {"x": "10", "y": "3"}
subtract_response = requests.get(f"{BASE_URL}/subtract", params=subtract_params)

print("Subtract Response:", subtract_response.json())