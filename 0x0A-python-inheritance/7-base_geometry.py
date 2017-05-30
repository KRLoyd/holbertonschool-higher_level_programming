#!/usr/bin/python3
"""Module to define class BaseGeometry."""


class BaseGeometry:
    """Class BaseGeometry"""
    
    def area(self):
        """method area
        
        Raises an Exception with the following message:
        message: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method integer_validator

        Validates value.

        Args:
        - name: name associated with value
        - value: object to be evaluated

        Exceptions Raised:
        - if value is not an integer: TypeError
        - if value <= 0: ValueError
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))
