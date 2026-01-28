#sort a dictionary by values
def sort_dict_by_values(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

# Example usage
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}
sorted_dict = sort_dict_by_values(my_dict)
print("Dictionary sorted by values:", sorted_dict)  # Output: Dictionary sorted by values: {'banana': 1, 'cherry': 2, 'apple': 3}