#convert decimal to binary using recursion
def decimal_to_binary(n):
    if n > 1:
        decimal_to_binary(n // 2)
    print(n % 2, end='')

# Example usage
decimal_to_binary(10)  # Output: 1010