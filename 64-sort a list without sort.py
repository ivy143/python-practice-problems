#sort a list without using the sort() function
def sort_list(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sort_list(numbers)
print("Sorted list:", numbers)