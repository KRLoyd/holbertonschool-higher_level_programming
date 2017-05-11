#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """ Finds all elements present in only one set

    Args: first set to evaluate, second set to evaluate

    Return: set of all elements in only one set
    """
    new_set = set_1 ^ set_2
    return new_set
