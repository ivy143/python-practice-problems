#find all permutations of a string
def find_permutations(s):
    if len(s) == 1:
        return [s]
    permutations = []
    for i, char in enumerate(s):
        for perm in find_permutations(s[:i] + s[i+1:]):
            permutations.append(char + perm)
    return permutations

# Example usage
string = "abc"
permutations = find_permutations(string)
for perm in permutations:
    print(perm)