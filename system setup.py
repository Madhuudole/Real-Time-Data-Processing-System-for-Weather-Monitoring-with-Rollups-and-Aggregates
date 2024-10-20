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
        return data
    else:
        print(f"Error: Unable to fetch data (status code {response.status_code}).")
        print(f"Response: {response.text}")
        return None

def test_system_setup():
    """
    Test if the system can connect to OpenWeatherMap API using a valid API key.
    """
    weather_data = get_weather('Delhi')
    assert weather_data is not None, "Error: Failed to connect to OpenWeatherMap API"
    print("System setup successful, API key is valid.")

# Test the system setup
test_system_setup()
