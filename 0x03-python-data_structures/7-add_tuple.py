#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """ My function to add 2 tuples

    Args: first tuple, second tuple

    Return: the sum of the 2 tuples
    """
    # Check tuple_a
    len_a = len(tuple_a)
    if len_a is 0:
        copy_a = (0, 0)
    elif len_a is 1:
        copy_a = (tuple_a[0], 0)
    else:
        copy_a = (tuple_a[0], tuple_a[1])
    # Check tuple_b
    len_b = len(tuple_b)
    if len_b is 0:
        copy_b = (0, 0)
    elif len_b is 1:
        copy_b = (tuple_b[0], 0)
    else:
        copy_b = (tuple_b[0], tuple_b[1])

    # Add approrpiate elements
    sum_a = copy_a[0] + copy_b[0]
    sum_b = copy_a[1] + copy_b[1]

    # Save addition to new-tuple and return
    new_tuple = (sum_a, sum_b)
    return new_tuple
