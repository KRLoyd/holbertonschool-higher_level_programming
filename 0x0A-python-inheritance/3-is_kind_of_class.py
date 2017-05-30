#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """function is_kind_of_class

    Checks if an object is an instance of, or if the object is an instance of a
    class that inherited from, the specified class.

    Args:
    - obj: object to evaluate
    - a_class: class to check against

    Returns:
    - True: object is an instance of or inherited from class
    - False: object is not an instance of or inherited from class
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
