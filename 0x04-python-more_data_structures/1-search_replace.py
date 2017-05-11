#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ My function to replace all occurance of an element with another

    Args: list to evaluate, element to replace, replacing element

    Return: copy of the original list with replacement(s) made
    """
    # Create empty list
    new_list = []
    # Traverse list and append correct elements to new_list
    for element in my_list:
        if element is search:
            new_list.append(replace)
        else:  # element is not search
            new_list.append(element)

    return new_list
