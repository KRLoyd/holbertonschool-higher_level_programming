#!/usr/bin/python3


def class_to_json(obj):
    """function class_to_json
    Returns the dictionary description with data structire for JSON object.

    Arg: obj - instance of a Class
    """
    return obj.__dict__
