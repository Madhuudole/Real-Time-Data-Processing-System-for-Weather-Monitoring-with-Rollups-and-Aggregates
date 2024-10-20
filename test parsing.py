import requests
import pandas as pd

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

def test_data_parsing(city):
    """
    Test the parsing and storing of weather data into a DataFrame.
    """
    weather_data = get_weather(city)
    
    if weather_data:
        # Parse data into a structured format (e.g., a dictionary)
        parsed_data = {
            'city': city,
            'temp': weather_data['main']['temp'],
            'feels_like': weather_data['main']['feels_like'],
            'weather_main': weather_data['weather'][0]['main'],
            'timestamp': weather_data['dt']
        }

        # Store parsed data in a pandas DataFrame
        df = pd.DataFrame([parsed_data])
        print(df)
        
        # Ensure data is stored correctly in DataFrame
        assert len(df) == 1, "Error: Data was not parsed and stored correctly"
    else:
        print("No weather data available.")

# Test data parsing for the city of 'Delhi'
test_data_parsing('Delhi')
