#!/usr/bin/python3
def multiple_returns(sentence):
    """ Returns a tuple with the lenght of a string and its first character

    Arg: sentence to evaluate

    Return: tuple with length of a string and its first character
    """
    # Check length of sentence
    s_len = len(sentence)

    # Find first character in sentence
    if s_len is 0:
        first_char = None
    else:
        first_char = sentence[0]

    # Create new tuple to return values of s_len and first_char
    return_tuple = (s_len, first_char)
    return return_tuple
