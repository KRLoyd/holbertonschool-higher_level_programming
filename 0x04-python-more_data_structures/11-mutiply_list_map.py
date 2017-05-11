#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    """ Multiplies all values by a number without a loop

    Args: list to be evaluated, number to multiply by

    Return: list of new values
    """
    new_list = list(map(lambda x: x * number, my_list))
    return new_list
