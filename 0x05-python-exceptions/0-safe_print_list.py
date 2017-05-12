#!/usr/bin/pyhon3
def safe_print_list(my_list=[], x=0):
    """ Prints specified elements of a list.

    Args: 
    my_list -- list to print
    x -- number of elements to print

    Return: number of elements printed
    """
    # Try to print the list
    try:
        printed = 0
        for i, element in enumerate(my_list):
            if i < x:
                print("{}".format(element), end="")
                printed += 1
                i += 1
    # Except: any error encountered
    except:
        pass
    # Always print new line and return printed
    finally:
        print()
        return printed
