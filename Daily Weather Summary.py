def test_daily_summary():
    temperatures = [300, 305, 298, 302]  # Simulated temp in Kelvin
    avg_temp = sum(temperatures) / len(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    
    print(f"Average Temp: {avg_temp - 273.15}, Max Temp: {max_temp - 273.15}, Min Temp: {min_temp - 273.15}")
    assert avg_temp > 0, "Error: Incorrect daily summary calculations"

test_daily_summary()
