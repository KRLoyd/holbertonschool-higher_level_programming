#!/usr/bin/python3
def best_score(my_dict):
    """ Finds the key with the biggest integer value

    Args: dictionary to evaluate

    Return: key with biggest integer value
    """
    # Make sorted list
    if my_dict:
        return(sorted(my_dict)[-1])
