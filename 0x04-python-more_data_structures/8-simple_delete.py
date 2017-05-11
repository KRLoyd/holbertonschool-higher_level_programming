#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    """ Deletes a key in a dictionary

    Args: dictionary to evaluate, key to delete

    Return: modified dictionary
    """
    # Check if key is in the dictionary
    if key in my_dict:
        # Delete key
        del my_dict[key]
    return my_dict
