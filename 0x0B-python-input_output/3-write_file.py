#!/usr/bin/python3


def write_file(filename="", text=""):
    """method write_file
    Writes text to file.
    Returns the number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        total_writ = f.write(text)
        return total_writ
