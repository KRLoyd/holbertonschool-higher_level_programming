#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    """ Prints a dictonary by ordered keys

    Arg: dictonary to evaluate
    """
    # Create ordered list of keys in dictonary
    sorted_list = sorted(my_dict.keys())

    # Print the list
    for key in sorted_list:
        value = my_dict[key]
        print("{}: {}".format(key, value))
