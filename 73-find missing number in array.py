#find missing number in an array
def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum

# Example usage
array = [1, 2, 4, 5, 6]
n = 6
print("Missing number:", find_missing_number(array, n))  # Output: Missing number: 3