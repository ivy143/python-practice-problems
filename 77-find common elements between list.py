#find common elements between two lists
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Example usage
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
print("Common elements:", find_common_elements(list_a, list_b))  # Output: Common elements: [4, 5]