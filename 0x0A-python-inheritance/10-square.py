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
        Rectangle.__width = size
        Rectangle.__height = size

    def area(self, size):
        """method area

        Returns the area of the square
        """
        return (self.__size ** 2)
