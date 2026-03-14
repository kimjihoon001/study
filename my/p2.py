import requests

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": "Seoul",
    "appid": "",
    "units": "metric"
}

response = requests.get(url, params=params)
data = response.json()


print(data)
# print("도시:", data["name"])
# print("온도:", data["main"]["temp"], "°C")
# print("습도:", data["main"]["humidity"], "%")
