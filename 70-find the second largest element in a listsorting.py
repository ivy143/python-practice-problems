#find the second largest element in a list using sorting
def second_largest_element(lst):
    if len(lst) < 2:
        return None  # Not enough elements for a second largest
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[1]

# Example usage
numbers = [10, 5, 8, 12, 7]
print("Second largest element:", second_largest_element(numbers))  # Output: Second largest element: 10