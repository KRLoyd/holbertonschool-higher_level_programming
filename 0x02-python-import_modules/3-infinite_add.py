#!/usr/bin/python
from sys import argv
if __name__ == "__main__":
    num_args = len(argv) - 1
    i = 1
    a = 0
    while i <= num_args:
        a = a + int(argv[i])
        i += 1
    print("{:d}".format(a))
