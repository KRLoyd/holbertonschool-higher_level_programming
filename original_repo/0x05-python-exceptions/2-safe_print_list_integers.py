#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ Prints the first x elements of a list, only integers

    Args:
    my_list -- list to print
    x -- number of elements to print

    Return: number of integers printed
    """
    # Start print counter at 0
    print_count = 0
    # For values up to x
    for i in range(0, x):
        # Try to print the element
        try:
            print("{:d}".format(my_list[i]), end="")
            print_count += 1
        # Exception for non integers
        except (TypeError, ValueError):
            continue
    print()
    return print_count
