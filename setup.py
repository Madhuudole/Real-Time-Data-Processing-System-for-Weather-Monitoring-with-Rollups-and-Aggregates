import time
import requests

API_KEY = 'b300f061dcebbae926a901539695441b'
cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

while True:
    for city in cities:
        weather_data = get_weather(city)
        # Process and store weather_data
    time.sleep(100) 
