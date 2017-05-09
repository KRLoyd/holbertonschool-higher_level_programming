#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """ My function to replace an element in a list at idx

    Args: list, idx to replace, replacing element

    Returns: modified list, or original list if idx is out of range
    """
    if idx >= len(my_list) or idx < 0 or len(my_list) == 0:
        return my_list
    else:
        my_list[idx] = element
        return my_list
