#edit distance
def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a matrix to store distances
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialize the matrix
    for i in range(m + 1):
        dp[i][0] = i  # Deletion
    for j in range(n + 1):
        dp[0][j] = j  # Insertion

    # Compute edit distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,    # Deletion
                               dp[i][j - 1] + 1,    # Insertion
                               dp[i - 1][j - 1] + 1) # Substitution

    return dp[m][n]
# Example usage
string1 = "kitten"
string2 = "sitting"
distance = edit_distance(string1, string2)
print(f"Edit distance between '{string1}' and '{string2}': {distance}")
