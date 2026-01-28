#validate parenthesis
def validate_parenthesis(expression):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return False
        else:
            continue

    return stack == []

# Example usage
expression = "{[()]}"
if validate_parenthesis(expression):
    print("Parentheses are balanced.")
else:
    print("Parentheses are not balanced.")
# Output: Parentheses are balanced.