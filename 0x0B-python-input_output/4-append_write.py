#!/usr/bin/python3
def append_write(filename="", text=""):
    """method append_write
    Appends a string at the end of a text file.

    Args:
    - filename: name of file
    - text: string to append

    Returns the number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        total_append = f.write(text)
        return total_append
