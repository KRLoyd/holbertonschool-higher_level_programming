#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """ Prints "My name is" and the first and last name

    Args:
    first_name -- name to print first after string
    last_name -- name to print after first
    """

    # Check if first_name is a string
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if last_name:
        if isinstance(last_name, str) is False:
            raise TypeError("last_name must be a string")

    # Print names in sentence
    print("My name is {:s} {:s}".format(first_name, last_name))
