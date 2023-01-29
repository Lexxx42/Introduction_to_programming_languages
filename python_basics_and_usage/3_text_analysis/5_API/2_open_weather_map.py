# Мы рассмотрим работу с API на примере open weather map.
# Это такой сервис, который предоставляет API для получения информации о погоде
# в разных точках планеты.

# Практически все сервисы, которые предоставляют доступ к API требуют API ключ.

import os
import requests
from dotenv import load_dotenv

API_URL = 'https://api.openweathermap.org/data/2.5/weather'
load_dotenv()
TOKEN = os.getenv('OPEN_WEATHER_TOKEN')

city = input('What is your city? ')

params = {
    'q': city,
    'appid': TOKEN,
    'units': 'metric',
}

response = requests.get(API_URL, params=params)
print(response.status_code)
print(response.headers['Content-Type'])
data = response.json()
print(f"Current temperature in {city} is {data['main']['temp']}")
