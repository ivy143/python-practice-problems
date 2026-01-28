#jump game problem
def can_jump(nums):
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    return True

# Example usage
nums = [2, 3, 1, 1, 4]
can_reach_end = can_jump(nums)
print("Can jump to the end:", can_reach_end)  # Output: Can jump to the end: True