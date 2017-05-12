#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ Divides element by element 2 lists

    Args:
    my_list_1 -- list to be divided
    my_list_2 -- divisor list
    list_length -- length of returned list

    Return: List of division results
    """
    # Create empty list to append results
    new_list = []
    # Iterate through the lists at same time
    for i in range(0, list_length):
        # Try to divide
        try:
            result = my_list_1[i] / my_list_2[i]
        # Exception for divide by 0
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        # Exception for not integer or float
        except IndexError:
            result = 0
            print("out of range")
        # Exception for wrong type
        except TypeError:
            result = 0
            print("wrong type")
        # Finally
        finally:
            new_list.append(result)
    return new_list
