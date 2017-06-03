#!/usr/bin/python3
import json
def from_json_string(my_str):
    """method from_json_string
    Returns an object represented by a JSON string.
    """
    py_obj = json.loads(my_str)
    return py_obj
