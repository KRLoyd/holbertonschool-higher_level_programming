#!/usr/bin/python3
""" 3-square module

Defines Square class
"""


class Square:
    """ Square class

    field: size
    """
    def __init__(self, size=0):
        """ __init__ module

        Instantiation of size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ area module

        Returns the current square area.
        """
        return (self.__size * self.__size)
