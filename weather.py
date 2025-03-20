import requests
from weather_api import api

userinput = input("enter full name of city: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={userinput}&appid={api}&units=metric"
weather_data = requests.get(url)
data = weather_data.json()
if weather_data.status_code == 200:
    weather = data["weather"][0]["main"]
    temperature = round(data["main"]["temp"])
    humidity = data["main"]["humidity"]
    country = data["sys"]["country"]
    print(f"weather in {userinput} is: ",weather)
    print(f"tempratrue in {userinput} is: {temperature}°F")
    print(f"humidity in {userinput} is: ",humidity)
    print(f"{userinput} located in : ",country)
else:
    print("No city found")
