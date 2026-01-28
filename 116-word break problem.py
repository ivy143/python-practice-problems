#word break problem
def word_break(s, word_dict):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[-1]

# Example usage
s = "leetcode"
word_dict = {"leet", "code"}
result = word_break(s, word_dict)
print("Can the word be segmented?", result)  # Output: Can the word be segmented? True
# Another example usage
s2 = "applepenapple"
word_dict2 = {"apple", "pen"}
result2 = word_break(s2, word_dict2)
print("Can the word be segmented?", result2)  # Output: Can the word be segmented? True