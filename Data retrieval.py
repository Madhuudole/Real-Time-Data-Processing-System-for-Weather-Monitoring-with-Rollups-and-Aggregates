import requests

# Replace with your actual API key from OpenWeatherMap
API_KEY = '7708d8b2b3187152708224d311785fe1'

# Function to retrieve weather data from OpenWeatherMap
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

# Function to test weather retrieval
def test_weather_retrieval(city):
    weather_data = get_weather(city)
    
    # Ensure weather data is not None and contains expected fields
    assert weather_data is not None, "Error: No weather data retrieved"
    assert 'main' in weather_data, "Error: 'main' key not found in the response"
    assert 'temp' in weather_data['main'], "Error: 'temp' key not found in the response"
    
    print(f"Weather data for {city} retrieved successfully!")
    print(weather_data)

# Test weather retrieval for a valid city
test_weather_retrieval('Mumbai')

