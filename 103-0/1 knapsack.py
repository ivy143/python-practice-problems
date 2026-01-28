#knapsack problem
def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]
# Example usage
weights = [1, 2, 3]
values = [10, 20, 30]
capacity = 5
max_value = knapsack(weights, values, capacity)
print(f"Maximum value that can be obtained: {max_value}")
# Output: Maximum value that can be obtained: 50
# Explanation:
# We can take items with weights 2 and 3 (values 20 + 30) to achieve the maximum value of 50 without exceeding the capacity of 5.