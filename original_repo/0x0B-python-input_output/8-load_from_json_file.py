#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """method load_from_json_file
    Creates an object from a JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
