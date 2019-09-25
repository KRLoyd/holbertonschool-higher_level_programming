#!/usr/bin/python3


def inherits_from(obj, a_class):
    """function inherits_from

    Checks if object is an instance of a class that inherited specific class

    Args:
    - obj: object to evaluate
    - a_class: class to compare to

    Returns:
    - True: object is an instance of a class that inherited specified class
    - False: object is an instance of a class that inherited specified class
    """
    if issubclass(type(obj), a_class) and not type(obj) == a_class:
        return True
    else:
        return False
