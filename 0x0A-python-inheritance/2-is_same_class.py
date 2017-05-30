#!/usr/bin/python3

def is_same_class(obj, a_class):
    """Function is_same_class
    Checks if an object is exactly an instance of specified class. 

    Args:
    - obj: object to evaluate
    - a_class: class to compare to

    Returns:
    - True: object is exactly an instance of class
    - False: object is not an exact instance of class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
