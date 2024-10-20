# Real-Time-Data-Processing-System-for-Weather-Monitoring-with-Rollups-and-Aggregates
ZEOTAP INTERN ASSIGNMENT TASK 2 :Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates

# Real-Time Weather Monitoring System

## Overview
This real-time weather monitoring system retrieves weather data from the OpenWeatherMap API and processes it to provide daily summaries, rollups, and alerts based on user-defined thresholds. The system can also retrieve weather forecasts and display summaries based on predicted conditions.

## Features
- **Real-time weather monitoring** for cities in India (e.g., Delhi, Mumbai, Bangalore).
- **Daily rollups and aggregates**: Calculate average, maximum, and minimum temperature, dominant weather condition, average humidity, and maximum wind speed.
- **Threshold-based alerts**: Get alerts when temperature or other weather conditions exceed user-defined thresholds.
- **Forecast summaries**: Retrieve and summarize the 5-day weather forecast.

---

## Prerequisites

### 1. Python
Ensure you have Python 3.6 or higher installed. You can download Python from the official [Python website](https://www.python.org/).

### 2. OpenWeatherMap API Key
You need an API key to access the OpenWeatherMap API. Follow the steps below to obtain the key:
1. Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).
2. Log in and navigate to the **API keys** section.
3. Create an API key and copy it for use in this project.

### 3. Install Required Python Packages
This project uses several Python libraries. You can install them by running the following command in your terminal:

```bash
pip install requests pandas matplotlib
```

Alternatively, if using Docker or virtual environments, make sure these dependencies are listed in the `requirements.txt` file:
```txt
requests
pandas
matplotlib
```

---

## Setup Instructions

### 1. Clone the Repository
To start working with this project, clone the repository:

```bash
git clone https://github.com/your-repo/real-time-weather-monitoring.git
cd real-time-weather-monitoring
```

### 2. Configure API Key
Edit the `weather_monitoring.py` file and replace the placeholder `your_api_key_here` with your actual API key from OpenWeatherMap.

```python
API_KEY = 'your_api_key_here'
```

### 3. Running the System
You can run the weather monitoring system by executing the main script:

```bash
python weather_monitoring.py
```

This will continuously retrieve weather data, calculate daily summaries, and check for threshold alerts based on the current conditions.

### 4. Configuring Thresholds (Optional)
You can configure custom thresholds for temperature alerts in the system. Inside `weather_monitoring.py`, modify the alert thresholds as follows:

```python
THRESHOLD_TEMP = 35  # Trigger alert if temperature exceeds 35°C
```

---

## Running Tests

You can run the test suite to validate the system’s functionality. Test cases include:
1. System setup and API connection.
2. Data retrieval and parsing.
3. Temperature conversion.
4. Daily rollups and threshold-based alerts.

To run the tests:

```bash
python -m unittest test_weather_monitoring.py
```

---

## Additional Features
- **Forecast summaries**: You can retrieve and generate summaries for the next 5 days by running:

```python
generate_forecast_summary('Mumbai')
```

- **Rollups for humidity and wind speed**: These are integrated into daily summaries and forecast summaries.

---

## Dependencies

- **requests**: For making API calls to the OpenWeatherMap API.
- **pandas**: For handling and analyzing weather data.
- **matplotlib**: For visualizing weather trends (optional, if you choose to add visualizations).

---

## Conclusion
This real-time weather monitoring system allows you to track and summarize weather data for various cities in India, with added support for forecast data and threshold-based alerts. You can further customize and extend the functionality by integrating more weather parameters or adding visualizations.

---

Let me know if you'd like to add more details or features!
## Objective:
Developing  a real-time data processing system to monitor weather conditions and provide
summarized insights using rollups and aggregates. The system will utilize data from the
OpenWeatherMap API (https://openweathermap.org/).
## Data Source:
The system will continuously retrieve weather data from the OpenWeatherMap API. You will
need to sign up for a free API key to access the data. The API provides various weather
parameters, and for this assignment, we will focus on:
● main: Main weather condition (e.g., Rain, Snow, Clear)
● temp: Current temperature in Centigrade
● feels_like: Perceived temperature in Centigrade
● dt: Time of the data update (Unix timestamp)
Processing and Analysis:
● The system should continuously call the OpenWeatherMap API at a configurable interval
(e.g., every 5 minutes) to retrieve real-time weather data for the metros in India. (Delhi,
Mumbai, Chennai, Bangalore, Kolkata, Hyderabad)
● For each received weather update:
○ Convert temperature values from Kelvin to Celsius (tip : you can also use user
preference).
Rollups and Aggregates:
1. Daily Weather Summary:
○ Roll up the weather data for each day.
○ Calculate daily aggregates for:
■ Average temperature
■ Maximum temperature
■ Minimum temperature
■ Dominant weather condition (give reason on this)
○ Store the daily summaries in a database or persistent storage for further analysis.
2. Alerting Thresholds:
○ Define user-configurable thresholds for temperature or specific weather
conditions (e.g., alert if temperature exceeds 35 degrees Celsius for two
consecutive updates).
○ Continuously track the latest weather data and compare it with the thresholds.
○ If a threshold is breached, trigger an alert for the current weather conditions.
Alerts could be displayed on the console or sent through an email notification
system (implementation details left open-ended).
3. Implement visualizations:
○ To display daily weather summaries, historical trends, and triggered alerts.
## Test Cases:
1. System Setup:
○ Verify system starts successfully and connects to the OpenWeatherMap API
using a valid API key.
2. Data Retrieval:
○ Simulate API calls at configurable intervals.
○ Ensure the system retrieves weather data for the specified location and parses
the response correctly.
3. Temperature Conversion:
○ Test conversion of temperature values from Kelvin to Celsius (or Fahrenheit)
based on user preference.
4. Daily Weather Summary:
○ Simulate a sequence of weather updates for several days.
○ Verify that daily summaries are calculated correctly, including average, maximum,
minimum temperatures,and dominant weather condition.
5. Alerting Thresholds:
○ Define and configure user thresholds for temperature or weather conditions.
○ Simulate weather data exceeding or breaching the thresholds.
○ Verify that alerts are triggered only when a threshold is violated.

## OUTPUT
http://127.0.0.1:5501/index.html
