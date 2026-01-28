#rotate an array by k steps
def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # In case k is greater than n
    return arr[-k:] + arr[:-k]
# Example usage
array = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotated_array = rotate_array(array, k)
print("Rotated array:", rotated_array)  # Output: Rotated array: [5, 6, 7, 1, 2, 3, 4]