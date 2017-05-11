#!/usr/bin/python3
def update_dictionary(my_dict, key, value):
    """ Replaces or adds key/value in a dictionary

    Args: dictionary to update, key to add/update, value to set key as

    Return: updated dictionary
    """
    my_dict[key] = value
    return my_dict
