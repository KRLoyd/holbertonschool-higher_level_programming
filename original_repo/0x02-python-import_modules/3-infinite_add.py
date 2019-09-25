#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_args = len(argv) - 1
    i = 1
    a = 0
    while i <= num_args:
        a = a + int(argv[i])
        i += 1
    print("{:d}".format(a))
