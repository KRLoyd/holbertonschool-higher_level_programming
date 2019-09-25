#!/usr/bin/python3
def text_indentation(text):
    """ Prints a text with 2 new lines after characters ., ?, and :

    Arg: text -- text to print
    """
    # Check that text is a string
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace(":", ":\n\n")
    text = text.replace("?", "?\n\n")
    text_list = text.split("\n")
    for sentence in range(0, len(text_list)):
        print("{:s}".format(text_list[sentence].strip()),
              end=("" if (sentence == (len(text_list) - 1)) else "\n"))
