#convert string to datetime
from datetime import datetime

date_string = input("Enter a date and time (e.g., 2023-08-15 14:30:00): ")
try:
    date_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    print(f"The converted datetime object is: {date_object}")
except ValueError:
    print("Invalid date format. Please use the format YYYY-MM-DD HH:MM:SS.")