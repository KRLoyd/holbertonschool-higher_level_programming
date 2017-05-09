#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """ My function that prints a matrix of integers

    Arg: matrix to print
    """
    # Check if matrix exists
    if matrix is None:
        return None

    # Check if matrix is empty
    if len(matrix[0]) is 0 and len(matrix) is 1:
        print()

    # Print the matrix
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print()
