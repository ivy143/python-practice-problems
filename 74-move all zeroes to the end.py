#move all zeroes to the end
def move_zeroes_to_end(arr):
    count = 0  # Count of non-zero elements
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < len(arr):
        arr[count] = 0
        count += 1
    return arr

# Example usage
array = [0, 1, 0, 3, 12]
print("Array after moving zeroes to the end:", move_zeroes_to_end(array))  # Output: Array after moving zeroes to the end: [1, 3, 12, 0, 0]