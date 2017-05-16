#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
    matrix -- matrix to evaluate
    div -- number to divide matrix elements by

    Return: new matrix with the result of division
    """
    # Check if div is 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if div is int or float
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")

    # Check that each row of matrix is the same size
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    # Create new_matrix
    new_matrix = []

    # Iterate through the matrix rows and elements to
    # check if element is not int or float
    for row in matrix:
        for element in row:
            if isinstance(element, (int, float)) is False:
                raise TypeError("matrix must be a "
                                "matrix (list of lists) of integers/floats")

    # Iterate through the matrix rows
    for row in matrix:
        # make new row with division
        new_row = list(map(lambda x: round((x / div), 2), row))
        # append new_row to new_matrix
        new_matrix.append(new_row)
    return new_matrix
