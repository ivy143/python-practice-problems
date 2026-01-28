#multiply two matrices using nested loops
def multiply_matrices(matrix_a, matrix_b):
    # Get the number of rows and columns for both matrices
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0]) if rows_a > 0 else 0
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0]) if rows_b > 0 else 0

    # Check if multiplication is possible (cols_a must equal rows_b)
    if cols_a != rows_b:
        raise ValueError("Number of columns in matrix A must equal number of rows in matrix B")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    # Perform matrix multiplication
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result

# Example usage
matrix_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_b = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result = multiply_matrices(matrix_a, matrix_b)
for row in result:
    print(row)