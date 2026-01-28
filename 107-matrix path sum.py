#matrix path sum problem
def matrix_path_sum(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]

    dp[0][0] = matrix[0][0]

    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]

    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[rows - 1][cols - 1]

# Example usage
matrix = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
result = matrix_path_sum(matrix)
print("Minimum path sum:", result)  # Output: Minimum path sum: 7