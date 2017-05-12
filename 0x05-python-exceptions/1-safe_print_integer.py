#!/usr/bin/python3
def safe_print_integer(value):
    """ Prints an integer with "{:d}".format()

    Arg:
    value -- to be printed

    Returns:
    True -- if value is an integer
    False -- if value is not an integer
    """
    # Try to print value
    try:
        print("{:d}".format(value))
        return True
    # Exception for value not integer
    except ValueError:
        return False
