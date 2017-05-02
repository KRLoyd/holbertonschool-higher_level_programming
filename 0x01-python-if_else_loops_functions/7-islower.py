#!/usr/bin/python3
def islower(c):
    # check if c is lowercase
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:  # not a lowercase character
        return False
