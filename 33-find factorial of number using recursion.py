#find factorial of number using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a non-negative integer: "))
print("Factorial of", num, "is:", factorial(num))