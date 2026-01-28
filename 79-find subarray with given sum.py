 #find subaaray with given sum
def find_subarray_with_sum(arr, target_sum):
    current_sum = 0
    start_index = 0

    for end_index in range(len(arr)):
        current_sum += arr[end_index]

        while current_sum > target_sum and start_index <= end_index:
            current_sum -= arr[start_index]
            start_index += 1

        if current_sum == target_sum:
            return arr[start_index:end_index + 1]

    return []  # No subarray found

# Example usage
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 15
result = find_subarray_with_sum(array, target_sum)
if result:
    print(f"Subarray with sum {target_sum} found:", result)
else:
    print(f"No subarray with sum {target_sum} found.")