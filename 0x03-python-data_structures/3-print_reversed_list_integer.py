#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ My function to print all integers of a list in reverse

    Arg: list to print
    """
    # Check if the list is empty
    if my_list is None:
        return
    # Not an empty list -> print the reverse
    for i in reversed(my_list):
        print("{:d}".format(i))
