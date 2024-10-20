import requests

API_KEY = '7708d8b2b3187152708224d311785fe1'
city = 'Delhi'

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        
        # Check if 'main' is in the response data
        if 'main' in data:
            return data
        else:
            print("Error: 'main' data not found in the response.")
            return None
    else:
        # Handle errors like invalid city or API key issues
        print(f"Error: Unable to fetch data (status code {response.status_code}).")
        print(f"Response: {response.text}")
        return None

weather_data = get_weather(city)

# Proceed only if weather_data is not None
if weather_data:
    # Extract the temperature in Kelvin from the API response
    kelvin_temp = weather_data['main']['temp']

    # Convert the temperature to Celsius
    celsius_temp = kelvin_temp - 273.15

    print(f"Temperature in Kelvin: {kelvin_temp} K")
    print(f"Temperature in Celsius: {celsius_temp:.2f} °C")
else:
    print("No weather data available.")
