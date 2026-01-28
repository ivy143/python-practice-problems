# Weather data analyzer
import csv
from collections import defaultdict
def analyze_weather_data(file_path):
    weather_data = defaultdict(lambda: {'total_temp': 0, 'total_humidity': 0, 'count': 0})

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            date = row['date']
            temp = float(row['temperature'])
            humidity = float(row['humidity'])
            weather_data[date]['total_temp'] += temp
            weather_data[date]['total_humidity'] += humidity
            weather_data[date]['count'] += 1

    # Calculate averages
    for date, data in weather_data.items():
        data['avg_temp'] = data['total_temp'] / data['count']
        data['avg_humidity'] = data['total_humidity'] / data['count']

    return weather_data
# Example usage
file_path = 'weather_data.csv'  # Path to your CSV file
weather_data = analyze_weather_data(file_path)
for date, data in weather_data.items():
    print(f"Date: {date}, Average Temperature: {data['avg_temp']:.2f}, Average Humidity: {data['avg_humidity']:.2f}")
# Example CSV content for testing:
# date,temperature,humidity
# 2024-04-01,22.5,60
# 2024-04-01,23.0,58
# 2024-04-02,21.0,65