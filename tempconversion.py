def test_temperature_conversion(kelvin_temp):
    celsius_temp = kelvin_temp - 273.15
    assert celsius_temp > -273.15, "Error: Temperature conversion is incorrect"
    print(f"Kelvin: {kelvin_temp}, Celsius: {celsius_temp}")

test_temperature_conversion(300)  # Example temperature in Kelvin
