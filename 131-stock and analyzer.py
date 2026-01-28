# Stock price analyzer
import csv
from collections import defaultdict
def analyze_stock_data(file_path):
    stock_data = defaultdict(lambda: {'total_close': 0, 'count': 0})

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            date = row['date']
            close_price = float(row['close'])
            stock_data[date]['total_close'] += close_price
            stock_data[date]['count'] += 1

    # Calculate average closing price per day
    for date, data in stock_data.items():
        data['avg_close'] = data['total_close'] / data['count']

    return stock_data
# Example usage
file_path = 'stock_data.csv'  # Path to your CSV file
stock_analysis = analyze_stock_data(file_path)
for date, data in stock_analysis.items():
    print(f"Date: {date}, Average Closing Price: {data['avg_close']:.2f}")
# Example CSV content for testing:
# date,open,high,low,close,volume
# 2024-04-01,100,105,99,104,10000
# 2024-04-01,102,106,101,105,15000
# 2024-04-02,103,107,102,106,20000
# Note: To run this code, you need to have a CSV file with stock data in the specified format.
# You can create a sample CSV file with the above content for testing purposes.
# The CSV file should have the following columns: date, open, high, low, close, volume
# Ensure that you have the required libraries installed.
# You can install the required libraries using:
# pip install pandas
# Although pandas is not used in this snippet, it can be helpful for more complex data analysis tasks.
# This code reads stock data from a CSV file, calculates the average closing price for each date, and prints the results.
# Make sure to replace 'stock_data.csv' with the path to your actual CSV file containing stock data.