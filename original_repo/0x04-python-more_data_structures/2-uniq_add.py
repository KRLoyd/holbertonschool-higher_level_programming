#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ My function to add all unique integers in a list

    Arg: list of integers to evaluate

    Return: Result of the addition
    """
    # Make list of unique elements in my_list
    uniq_list = set(my_list)

    a = 0
    # Traverse uniq_list and add all elements together
    for element in uniq_list:
        a += element
    return a
