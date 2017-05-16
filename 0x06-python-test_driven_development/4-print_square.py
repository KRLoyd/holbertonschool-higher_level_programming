#!/usr/bin/python3
def print_square(size):
    """ Prints a square with the character #

    Arg: size -- size of square to print
    """
    # Check if size is integer
    if isinstance(size, (int, float)) is False:
        raise TypeError("size must be an integer")

    # Check if size is float < 0
    if isinstance(size, float) is True:
        if size < 0:
            raise TypeError("size must be an integer")
        else:  # change float to int
            size = int(size)
    
    # Check if size < 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for row in range(0, size):
        print("{:s}".format("#" * size))
