#!/usr/bin/python3
def max_integer(my_list=[]):
    """ My function to find the largest integer of a list

    Arg: list to evaluate
    Return: biggest integer in the list (SUCCESS), None if list is empty
    """
    list_len = len(my_list)
    if list_len is 0:
        return None

    temp = 0;
    i = 0
    while i < list_len - 1:
        if my_list[i] > temp:
            temp = my_list[i]
        i += 1

    return temp
