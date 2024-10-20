temperatures = [30.1, 30.5, 30.2, 30.7]  # Example temperatures

# Calculate the average temperature
avg_temp = sum(temperatures) / len(temperatures)

# Debug: Print the temperatures and calculated average
print(f"Collected temperatures: {temperatures}")
print(f"Calculated average temperature: {avg_temp}")

# Use an assertion with a tolerance for floating-point precision
assert abs(avg_temp - 30.38) < 0.01, f"Error: Average temperature is incorrect. Expected 30.38 but got {avg_temp}"