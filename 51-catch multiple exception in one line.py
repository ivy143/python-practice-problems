#program to catch multiple exceptions in one line
try:
    # Code that may raise multiple exceptions
    x = int(input("Enter a number: "))
    y = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
else:
    print(f"Result: {y}")
input("Press Enter to continue...")