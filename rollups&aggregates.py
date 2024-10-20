import pandas as pd
from datetime import datetime

# A list to store daily weather data
daily_data = []

def update_daily_summary(weather_data):
    """
    Update the daily weather summary with new weather data.
    """
    # Append the current weather data to daily records
    daily_data.append(weather_data)

    # Create a DataFrame for the daily data
    df = pd.DataFrame(daily_data)

    # Perform rollups/aggregates for the day
    avg_temp = df['temp'].mean()
    max_temp = df['temp'].max()
    min_temp = df['temp'].min()
    avg_humidity = df['humidity'].mean()  # New: Average Humidity
    max_wind_speed = df['wind_speed'].max()  # New: Maximum Wind Speed
    dominant_condition = df['weather_main'].mode()[0]  # Most common weather condition
    
    daily_summary = {
        'date': datetime.now().date(),
        'avg_temp': avg_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'avg_humidity': avg_humidity,
        'max_wind_speed': max_wind_speed,
        'dominant_condition': dominant_condition
    }
    
    print("Daily Summary:", daily_summary)
    return daily_summary
