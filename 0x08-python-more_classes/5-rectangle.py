#!/usr/bin/python3
""" Module to define class Rectangle """


class Rectangle:
    """ Rectangle class"""

    def __init__(self, width=0, height=0):
        """ __init__ method

        Instantiation of width.
        Instantiation of height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width method (get)

        Retrieves width.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ width method (set)

        Sets width.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height method (get)

        Retrieves height.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ height method (set)

        Sets height.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area method

        Returns area of the rectangle.
        """
        return  (self.__width * self.__height)

    def perimeter(self):
        """ perimeter method

        Returns the rectangle perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ __str__ method

        Returns representation of the rectangle with # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        str_rectangle = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                str_rectangle += "#"
            if i != self.__height - 1:
                str_rectangle += "\n"
        return (str_rectangle)

    def __repr__(self):
        """ __repr__ method

        Returns a string representation of the rectangle.
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """ __del__ method

        Prints a message when an instance is deleted.
        """
        print("Bye rectangle...")
