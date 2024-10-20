def test_alerting_threshold():
    threshold_temp = 35  # 35 degrees Celsius threshold
    temperatures = [30, 36, 34]  # Simulated temperatures in Celsius
    
    for temp in temperatures:
        if temp > threshold_temp:
            print(f"Alert: Temperature {temp}°C exceeds the threshold of {threshold_temp}°C!")
        else:
            print(f"Temperature {temp}°C is within safe limits.")
    
    assert any(temp > threshold_temp for temp in temperatures), "Error: No alerts triggered"

test_alerting_threshold()
