#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

empty_matrix = [[]]

# Holberton tests
# Print matrix
print_matrix_integer(matrix)
print("--")
# Print but no arg
print_matrix_integer()
print("--")

# Print empty matrix
print_matrix_integer(empty_matrix)
print("--")
