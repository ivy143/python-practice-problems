#remove duplicates from a sorted array
def remove_duplicates(sorted_arr):
    if not sorted_arr:
        return []

    unique_arr = [sorted_arr[0]]
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] != sorted_arr[i - 1]:
            unique_arr.append(sorted_arr[i])

    return unique_arr

# Example usage
sorted_array = [1, 1, 2, 2, 3, 4, 4, 5]
print("Array after removing duplicates:", remove_duplicates(sorted_array))  # Output: Array after removing duplicates: [1, 2, 3, 4, 5]