#!/usr/bin/python3
"""Module to define MyList class"""


class MyList(list):
    """Class MyList.
    Parent class: list.
    """

    def print_sorted(self):
        """print_sorted method
        Prints the list in acending order."""
        print(sorted(self))
