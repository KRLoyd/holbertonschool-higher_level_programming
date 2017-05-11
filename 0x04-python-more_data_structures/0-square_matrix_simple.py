#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ My function that computes the square value of all integers of a matrix.

    Arg: matrix to evaluate

    Return: new matrix, each value is the square value of input
    """
    # Check if matrix exists
    if matrix is None:
        return None
    # Check if matrix is empty
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print()
        return

    # Create new_matrix
    new_matrix = []

    # Iterate through matrix rows
    for row in matrix:
        # make new_row
        new_row = list(map(lambda x: x**2, row))
        # append new_row to new_matrix
        new_matrix.append(new_row)
    return new_matrix
