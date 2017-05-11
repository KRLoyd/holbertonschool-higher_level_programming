#!/usr/bin/python3
def best_score(my_dict):
    """ Finds the key with the biggest integer value

    Args: dictionary to evaluate

    Return: key with biggest integer value
    """

    # Check if dictionary exists
    if my_dict is None:
        return None

    largest = 0
    # Loop through the dictionary and compare values
    for key, value in my_dict.items():
        if value > largest:
            largest = value
            largest_key = key

    return largest_key
