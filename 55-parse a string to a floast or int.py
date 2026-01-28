#parse a string to a float or int
try:
    user_input = input("Enter a number: ")
    if '.' in user_input:
        number = float(user_input)
    else:
        number = int(user_input)
    print(f"The parsed number is {number} and its type is {type(number)}")
except ValueError:
    print("Invalid input! Please enter a valid number.")