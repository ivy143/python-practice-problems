#program to demonstrate slicing in loops
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop through the list in slices of size 3
slice_size = 3
for i in range(0, len(my_list), slice_size):
    slice = my_list[i:i+slice_size]
    print(slice)