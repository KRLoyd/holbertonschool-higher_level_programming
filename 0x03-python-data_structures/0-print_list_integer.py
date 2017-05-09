#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """ My function to print all integers of a list

    Arg: list to print
    """
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
