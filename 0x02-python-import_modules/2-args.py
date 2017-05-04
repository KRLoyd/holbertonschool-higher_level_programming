#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    # find the number of arguments and save to a variable
    num_arg = len(argv) - 1
    # check for no arguments
    if num_arg == 0:
        print("{:d} argument.".format(num_arg))
    # if arguments, print them
    else:  # num_arg > 0
        print("{:d} arguments:".format(num_arg))
        i = 1
        # traverse the list of arguments
        while i <= num_arg:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1
