import pandas as pd
import requests

# Replace with your actual API key
API_KEY = '7708d8b2b3187152708224d311785fe1'

def get_weather_forecast(city):
    """
    Retrieves the 5-day weather forecast data for the given city from the OpenWeatherMap API.
    """
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}'
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        forecast_list = data['list']  # This contains the forecast data for multiple timestamps

        # Parse the forecast data to extract important fields
        forecast_data = []
        for forecast in forecast_list:
            forecast_data.append({
                'timestamp': forecast['dt'],
                'temp': forecast['main']['temp'],
                'feels_like': forecast['main']['feels_like'],
                'weather_main': forecast['weather'][0]['main'],
                'humidity': forecast['main']['humidity'],
                'wind_speed': forecast['wind']['speed']
            })
        return forecast_data
    else:
        print(f"Error: Unable to fetch forecast data (status code {response.status_code}).")
        return None
# Test forecast summary for a city
forecast_data = get_weather_forecast('Mumbai')

# Ensure that forecast data is retrieved and print it
if forecast_data:
    for forecast in forecast_data:
        print(forecast)
else:
    print("No forecast data available.")
