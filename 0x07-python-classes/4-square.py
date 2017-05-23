#!/usr/bin/python3
""" 4-square module

Defines Square class and modules
"""


class Square:
    """ Square class

    Modules:
    - __init__
    - size (to retrieve)
    - size (to set)
    - area
    """

    def __init__(self, size=0):
        """ __init__ module

        Instantiation of size.
        """
        # new_size = Square.size(self, size)
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ size module (get)

        Retrieve the size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ size module (set)

        Sets size to value.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ area module

        Returns the current square area.
        """
        return (self.__size * self.__size)
