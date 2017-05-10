#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """ My function to delete the item at a specified position.

    Args: list to evaluate, position to delete

    Return: modified list
    """
    list_len = len(my_list)

    # Check that list exists
    if my_list is None:
        return None
    # Check if list is empty
    if list_len is 0:
        return my_list
    # Check that idx is not out of range
    if idx <= list_len and idx > 0:
        # Delete specified index
        copy_list = my_list
        del(copy_list[idx])
    else:
        return my_list
    # Return modified list
    return copy_list
