#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ My function to print all integers of a list in reverse

    Arg: list to print
    """
    if len(my_list) == 0:
        return
    for i in reversed(my_list):
        print("{:d}".format(i))
