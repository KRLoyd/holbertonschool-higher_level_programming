#!/usr/bin/python3
def number_keys(my_dict):
    """ Finds the number of keys in a dictonary

    Arg: dictonary to evaluate

    Return: number of keys in the dictonary
    """

    # Make list from keys in dictonary
    key_list = list(my_dict.keys())
    # Count the number of keys in the list
    total_keys = 0
    for keys in key_list:
        total_keys += 1

    return total_keys
