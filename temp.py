def test_temperature_conversion(kelvin_temp):
    celsius_temp = kelvin_temp - 273.15
    assert celsius_temp == round(kelvin_temp - 273.15, 2), "Error: Temperature conversion is incorrect"
    print(f"Temperature conversion successful: {kelvin_temp}K = {celsius_temp:.2f}°C")

# Test temperature conversion
test_temperature_conversion(300.15)  # Example Kelvin value
