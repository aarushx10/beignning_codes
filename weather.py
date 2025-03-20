import requests
from weather_api import api

userinput = input("enter city: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={userinput}&appid={api}&units=metric"
weather_data = requests.get(url)
data = weather_data.json()
if weather_data.status_code == 200:
    weather = data["weather"][0]["main"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    country = data["sys"]["country"]
    print("weather is: ",weather)
    print("tempratrue is: ",temperature)
    print("humidity is: ",humidity)
    print("country is: ",country)


"""'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]
'main': {'temp': 35.16, 'feels_like': 32.45, 'temp_min': 35.16, 'temp_max': 35.16, 'pressure': 1010, 'humidity': 9, 'sea_level': 1010, 'grnd_level': 990}"""