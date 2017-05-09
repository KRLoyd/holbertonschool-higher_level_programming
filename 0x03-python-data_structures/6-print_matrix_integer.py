#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """ My function that prints a matrix of integers

    Arg: matrix to print
    """
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print()
