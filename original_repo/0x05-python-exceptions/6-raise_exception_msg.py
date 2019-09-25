#!/usr/bin/python3
def raise_exception_msg(message=""):
    """ Raises a name exception with a message.

    Arg:
    message -- message to print when raising name exception
    """
    try:
        raise NameError(message)
    except NameError:
        raise
