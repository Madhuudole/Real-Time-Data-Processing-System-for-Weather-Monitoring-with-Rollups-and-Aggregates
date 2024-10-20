def test_alerting_system():
    alert_threshold = 35  # Celsius
    consecutive_exceeding_updates = 0
    
    # Simulated weather updates
    weather_updates = [34, 36, 37, 33]  # Temperatures in Celsius
    
    for temp in weather_updates:
        if temp > alert_threshold:
            consecutive_exceeding_updates += 1
            if consecutive_exceeding_updates >= 2:
                print(f"ALERT: Temperature exceeded {alert_threshold}°C for two consecutive updates!")
                assert True
        else:
            consecutive_exceeding_updates = 0
    
# Test alerting system
test_alerting_system()
