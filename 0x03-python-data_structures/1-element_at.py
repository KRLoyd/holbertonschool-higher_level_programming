#!/usr/bin/python3
def element_at(my_list, idx):
    """ My function to retrieve an element from a list

    Args: list to evaluate, element to retrieve

    Return: element at idx
    """
    print("len(my_list): {:d}".format(-len(my_list)))
    if idx > len(my_list) or idx < -(len(my_list)):
        return None
    else:
        return my_list[idx]
