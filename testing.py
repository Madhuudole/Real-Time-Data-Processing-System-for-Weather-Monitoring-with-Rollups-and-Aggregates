def get_weather(city):
    def test_weather_retrieval(city):
        weather_data = get_weather(city)
    
    # Ensure weather data is not None and contains expected fields
        assert weather_data is not None, "Error: No weather data retrieved"
        assert 'main' in weather_data, "Error: 'main' key not found in the response"
        assert 'temp' in weather_data['main'], "Error: 'temp' key not found in the response"
        print(f"Weather data for {city} retrieved successfully!")
    

city = 'Delhi'
weather_data = get_weather(city)

if weather_data:
    print("Weather data retrieved successfully!")
    print(weather_data)  # Display the raw weather data (for debugging)
else:
    print("No weather data available.")

