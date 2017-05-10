#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """ My function that finds all multiples of 2 in a list

    Arg: list to evaluate

    Return: list with "True" or "False" depending on if the integer at that 
    same position in the original list is a multiple of 2.
    """
    result_list = []
    for i in my_list:
        if i % 2 is 0:
            result_list.append(True)
        else:  # integer isn't divisible by 2
            result_list.append(False)
    return result_list
