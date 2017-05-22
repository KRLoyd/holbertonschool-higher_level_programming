#!/usr/bin/python3
""" 6-square module

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

    def __init__(self, size=0, position=(0, 0)):
        """ __init__ module

        Instantiation of size.
        Instantiation of position.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ position module (get)

        Retrieve the position of the square.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ position module (set)

        Sets position to value.
        """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for x in value:
            if type(x) is not int:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            if x < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ area module

        Returns the current square area.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ my_print module

        Prints in stdout the square with character #.
        """
        if self.__size == 0:
            print()
        if self.__position:
            for i in range(0, self.__position[1]):
                print(" ")
        for row in range(0, self.__size):
            if self.__position:
                print(" " * self.__position[0], end="")
            for column in range(0, self.__size):
                if column == self.__size - 1:
                    print("#")
                else:
                    print("#", end="")
