#!/usr/bin/python3
def multiply_by_2(my_dict):
    """ Returns a new dictionary with all values multiplied by 2

    Arg: dictionary to evaluate

    Return: new dictionary
    """
    # Create empty dictionary
    new_dict = {}
    # Iterate through original dictionary
    for key in my_dict:
        # Multiply value by 2
        value = (my_dict[key] * 2)
        # add key and new value to new_dictionary
        new_dict[key] = value

    return new_dict
