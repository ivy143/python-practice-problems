#merge two dictionaries
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary
    merged_dict.update(dict2)   # Update with the second dictionary
    return merged_dict

# Example usage
dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}
print("Merged dictionary:", merge_dictionaries(dict_a, dict_b))  # Output: Merged dictionary: {'a': 1, 'b': 3, 'c': 4}