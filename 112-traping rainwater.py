#trapping rainwater problem
def trap_rainwater(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    trapped_water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            trapped_water += max(0, left_max - height[left])
        else:
            right -= 1
            right_max = max(right_max, height[right])
            trapped_water += max(0, right_max - height[right])

    return trapped_water

# Example usage
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
result = trap_rainwater(height)
print("Trapped rainwater:", result)  # Output: Trapped rainwater: 6