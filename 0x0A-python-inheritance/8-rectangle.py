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
