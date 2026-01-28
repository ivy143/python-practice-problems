#find intersection of two arrays
def find_intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))
# Example usage
array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]
print("Intersection of arrays:", find_intersection(array1, array2))  # Output: Intersection of arrays: [4, 5]