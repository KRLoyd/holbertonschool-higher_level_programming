#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """method read_lines
    Reads n lines of a text file.

    Args:
    - filename
    - number of lines to print
    """

    line_count = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        for lines in f:
            line_count += 1
    with open(filename, mode='r', encoding='utf-8') as f:
        if nb_lines <= 0 or nb_lines >= line_count:
            result = f.read()
            print("{:s}".format(result), end="")
        else:
            for j, line in enumerate(f):
                if j < nb_lines:
                    print("{:s}".format(line), end="")
