 #making and displaying calendar of any year
import calendar

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

print(calendar.month(year, month))