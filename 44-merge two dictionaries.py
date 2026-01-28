#program to merge two dictionaries in Python
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary
    merged_dict.update(dict2)   # Update with the second dictionary
    return merged_dict

# Example usage
dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}

merged = merge_dictionaries(dict_a, dict_b)
print("Merged dictionary:", merged)