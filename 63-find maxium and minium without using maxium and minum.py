#find maximum and minimum without using maximum and minimum functions
def find_max_min(arr):
    if len(arr) == 0:
        return None, None  # Handle empty array case

    max_val = arr[0]
    min_val = arr[0]

    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val
# Example usage
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
maximum, minimum = find_max_min(numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)