#program to copy a file in Python
try:
	string = input("enter something here:")
	num = int(input("enter a number here:"))
	print(string * num)


	string = input("enter something here:")
	num = int(input("enter a number here:"))
	print(string + str(num))
except (TypeError, ValueError) as a:
	print(f"An error occurred: {a}")