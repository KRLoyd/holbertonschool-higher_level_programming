#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ My function that replaces an element in a list.
    The original list is not modified.

    Args: list, index of element to replace, the replacing value

    Returns: modified list (SUCCESS), or copy of original list (FAILURE)
    """
    copy = my_list[:]

    if my_list is None:
        return copy
    if idx >= len(my_list) or idx < 0:
        return copy
    copy[idx] = element
    return copy
