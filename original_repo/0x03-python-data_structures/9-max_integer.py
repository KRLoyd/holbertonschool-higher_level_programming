#!/usr/bin/python3
def max_integer(my_list=[]):
    """ My function to find the largest integer of a list

    Arg: list to evaluate
    Return: biggest integer in the list (SUCCESS), None if list is empty
    """
    # Check if list exists
    if my_list is None:
        return None
    # Check if empty list
    list_len = len(my_list)
    if list_len is 0:
        return None
    # List isn't empty
    temp = my_list[0]
    i = 0
    while i < list_len:
        if my_list[i] > temp:
            temp = my_list[i]
        i += 1

    return temp
