#!/usr/bin/python3
def uppercase(str):
    for i in str[:]:
        # check if character is lowercase
        if ord(i) > 96 and ord(i) < 123:
            print("{:s}".format(chr(ord(i) - 32)), end="")
        else:  # if character is not lowercase
            print("{:s}".format(i), end="")
    print()
