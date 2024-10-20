import requests

# Replace with your actual API key from OpenWeatherMap
API_KEY = '7708d8b2b3187152708224d311785fe1'

def get_weather(city):
    """
    Retrieves the current weather data for the given city from the OpenWeatherMap API.
    """
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Extract the required weather data, including additional parameters
        weather_data = {
            'city': city,
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'weather_main': data['weather'][0]['main'],
            'humidity': data['main']['humidity'],     # New: Humidity
            'wind_speed': data['wind']['speed'],      # New: Wind Speed
            'timestamp': data['dt']
        }
        return weather_data
    else:
        print(f"Error: Unable to fetch data (status code {response.status_code}).")
        return None
