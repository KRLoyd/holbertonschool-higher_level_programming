#!/usr/bin/python3
def islower(c):
# check if c is lowercase
    if ord(c) > 97 and ord(c) < 122:
        return True
    else:  # not a lowercase character
        return False
