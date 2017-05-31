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
