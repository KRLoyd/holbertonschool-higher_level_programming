#!/usr/bin/pyhon3
def safe_print_list(my_list=[], x=0):
    """ Prints specified elements of a list.

    Args:
    my_list -- list to print
    x -- number of elements to print

    Return: number of elements printed
    """
    # Set print counter to 0
    printed = 0
    # Iterate up to x
    for i in range(0, x):
        # Try to print the list
        try:
            print("{}".format(my_list[i]), end="")
            printed += 1
        # Handle exceptions
        except (NameError, IndexError, TypeError):
            break
    # Always print a new line
    print()
    return printed
