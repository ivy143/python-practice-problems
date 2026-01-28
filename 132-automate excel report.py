# Automate Excel report generation
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
def generate_excel_report(data, report_path):
    # Create a new workbook and select the active worksheet
    wb = Workbook()
    ws = wb.active
    ws.title = "Report"

    # Define header
    headers = list(data[0].keys())
    ws.append(headers)

    # Apply styles to header
    for col in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col)
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal='center')

    # Add data to worksheet
    for row_data in data:
        ws.append(list(row_data.values()))

    # Adjust column widths
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter  # Get the column name
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2)
        ws.column_dimensions[column].width = adjusted_width

    # Save the workbook to the specified path
    wb.save(report_path)
# Example usage
data = [
    {"Name": "Alice", "Age": 30, "City": "New York"},
    {"Name": "Bob", "Age": 25, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 35, "City": "Chicago"}
]
report_path = "example_report.xlsx"
generate_excel_report(data, report_path)
print(f"Excel report generated at: {report_path}")
# This code creates an Excel report from a list of dictionaries using openpyxl. It styles the header, adjusts column widths, and saves the file to the specified path.
# Make sure to have the required libraries installed:
# pip install openpyxl pandas
# Note: You can customize the data and report path as needed for your specific use case.