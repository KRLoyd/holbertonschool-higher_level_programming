#!/usr/bin/python3
import json
def to_json_string(my_obj):
    """method to_json_string
    Returns JSON representation of an object.
    """
    jsn_str = json.dumps(my_obj)
    return jsn_str
