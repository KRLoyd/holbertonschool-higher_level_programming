#!/usr/bin/python3
def number_of_lines(filename=""):
    """method number_of_lines
    Returns the number of lines in a text file.
    """
    lines = 0;
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            lines += 1
    return lines
