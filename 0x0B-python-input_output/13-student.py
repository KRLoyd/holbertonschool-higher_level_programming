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

    def to_json(self, attrs=None):
        """method to_json

        Returns a dictionary representation of Student instance.
        """
        new_dict = {}
        if attrs is not None and type(attrs) is list:
            for i in attrs:
                if type(i) is str:
                    if hasattr(self, i) is True:
                        value = getattr(self, i)
                        new_dict[i] = value
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """method reload_from_json

        Replaces all attributes of the Student instance.
        Replacing values are in dictionary json.
        """
        if 'first_name' in json:
            self.first_name = json['first_name']
        if 'last_name' in json:
            self.last_name = json['last_name']
        if 'age' in json:
            self.age = json['age']
