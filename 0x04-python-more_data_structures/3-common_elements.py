#!/usr/bin/python3
def common_elements(set_1, set_2):
    """ Returns a set of common elements in two sets

    Args: first set, second set

    Return: set of common elements in the sets
    """
    new_set = set_1 & set_2
    return new_set
