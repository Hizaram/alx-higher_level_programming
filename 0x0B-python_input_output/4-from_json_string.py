#!/usr/bin/python3
"""Function that returns an object from JSON string"""
import json


def from_json_string(my_str):
    """Converts JSON string to a Python Object
    Args:
        my_str (JSON string): JSON str to be converted
    Returns:
        Python representation of object
    """
    return json.loads(my_str)
