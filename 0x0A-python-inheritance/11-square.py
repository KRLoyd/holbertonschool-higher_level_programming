#!/usr/bin/python
"""method to define class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """method __init__

        Instantiation of size.
        """
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)
        self.__width = size
        self.__height = size

    def __str__(self):
        """method __str__

        Prints square description in the following format:
        [Square] <width>/<height>
        """
        sq_width = str(self.__width)
        sq_height = str(self.__height)
        sq_return = "" + "[Square] " + sq_width + "/" + sq_height
        return sq_return
