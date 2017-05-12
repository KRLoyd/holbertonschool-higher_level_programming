#!/usr/bin/python3
def safe_print_division(a, b):
    """ Divides 2 integers and prints the result

    Args:
    a -- first integer
    b -- second integer

    Return:
    Success -- value of division
    Failure -- None
    """

    # Try the division
    try:
        result = a / b
    # Handle exceptions
    except ZeroDivisionError:
        result = None
    # Finally - print result of division
    finally:
        print("Inside result: {}".format(result))
        return result
