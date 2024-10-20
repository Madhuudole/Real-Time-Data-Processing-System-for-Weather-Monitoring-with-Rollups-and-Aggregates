alert_threshold = 35  # Celsius
def check_alerts(temp):
    if temp > alert_threshold:
        print(f"ALERT: Temperature exceeded {alert_threshold}°C!")
import smtplib

def send_email_alert(subject, message, to_email):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_password")
    body = f'Subject: {subject}\n\n{message}'
    server.sendmail("your_email@gmail.com", to_email, body)
    server.quit()
import matplotlib.pyplot as plt

def plot_weather_trends(dates, temps):
    plt.plot(dates, temps)
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Trends')
    plt.show()
