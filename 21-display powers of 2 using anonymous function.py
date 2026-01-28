num_terms = int(input("Enter the number of terms to display powers of 2: "))
powers_of_2 = list(map(lambda x: 2 ** x, range(num_terms)))
for power in powers_of_2:
    print(power)