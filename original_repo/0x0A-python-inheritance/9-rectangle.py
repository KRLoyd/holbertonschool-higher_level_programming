#!/usr/bin/python3
"""module to define class Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle

    Parent class: BaseGeometry (module 7-base_geometry.py)
    """
    def __init__(self, width, height):
        """method __init__

        Instantiation of:
        - width
        - height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method area

        Returns rectangle's width * height
        """
        return (self.__width * self.__height)

    def __str__(self):
        """method __str__

        Prints description in following format:
        [Rectangle] <width>/<height>
        """
        str_width = str(self.__width)
        str_height = str(self.__height)
        str_rect = "" + "[Rectangle] " + str_width + "/" + str_height
        return str_rect
