#transpose a matrix
def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = transpose_matrix(matrix)
print("Original matrix:")
for row in matrix:
    print(row)
print("Transposed matrix:")
for row in transposed:
    print(row)  # Output: Transposed matrix: [1, 4, 7], [2, 5, 8], [3, 6, 9]