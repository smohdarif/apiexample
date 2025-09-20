import requests

url = "https://apiexample-d0f4.onrender.com/add"

querystring = {"x":"5","y":"5"}

response = requests.get(url, params=querystring)

print(response.json())