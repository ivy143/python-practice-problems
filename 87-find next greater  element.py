#find next greater element
def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)

    return result

# Example usage
arr = [4, 5, 2, 25]
print("Next greater elements:", next_greater_element(arr))  # Output: Next greater elements: [5, 25, 25, -1]