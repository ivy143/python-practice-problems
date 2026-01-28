#illustrate different set operations using Python sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union
union_set = set_a.union(set_b)
print("Union:", union_set)

# Intersection
intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)

# Difference
difference_set = set_a.difference(set_b)
print("Difference (A - B):", difference_set)

# Symmetric Difference
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", symmetric_difference_set)