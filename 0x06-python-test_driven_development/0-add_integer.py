#!/usr/bin/python3
def add_integer(a, b):
    """
    Adds 2 integers.

    Args:
    a -- first integer
    b -- second integer

    Return: integer result of a and b
    """
    if isinstance(a, (int, float, complex)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float, complex)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
