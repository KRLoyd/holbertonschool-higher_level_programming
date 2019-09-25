#!/usr/bin/python3
def read_file(filename=""):
    """method read_file
    Reads a text file and prints it to stdout.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print("{:s}".format(content), end="")
