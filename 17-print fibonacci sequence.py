num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
n1, n2 = 0, 1
count = 0

while count < num_terms:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1