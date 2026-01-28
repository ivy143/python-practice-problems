# Analyze CSV data for sales problem
import csv
from collections import defaultdict
def analyze_sales_data(file_path):
    sales_data = defaultdict(lambda: {'total_sales': 0, 'total_quantity': 0})

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            product = row['product']
            quantity = int(row['quantity'])
            price = float(row['price'])
            sales_data[product]['total_sales'] += price * quantity
            sales_data[product]['total_quantity'] += quantity

    return sales_data
# Example usage
file_path = 'sales_data.csv'  # Path to your CSV file
result = analyze_sales_data(file_path)
for product, data in result.items():
    print(f"Product: {product}, Total Sales: {data['total_sales']}, Total Quantity: {data['total_quantity']}")
# Example CSV content for testing:
# product,quantity,price
# apple,10,1.5
# banana,5,0.8
# orange,8,1.2
# apple,7,1.5
# banana,3,0.8
# Expected Output:
# Product: apple, Total Sales: 25.5, Total Quantity: 17