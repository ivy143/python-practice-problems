#program to sort a dictionary by value in Python
my_dict = {'a': 3, 'b': 1, 'c': 2}

# Sort the dictionary by value
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print("Sorted dictionary by value:", sorted_dict)