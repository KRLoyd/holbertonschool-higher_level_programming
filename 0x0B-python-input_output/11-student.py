#!/usr/bin/python3
"""module to define class Student"""


class Student():
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """method __init__

        Instantiates the following public instance attributes:
        - first_name
        - last_name
        - age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method to_json

        Returns a dictionary representation of Student instance.
        """
        return self.__dict__
