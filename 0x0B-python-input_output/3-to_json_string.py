#!/usr/bin/python3
"""Function that converts an object to JSON representation"""
import json


def to_json_string(my_obj):
    """Converts my_obj to its json equivalent
    Args:
        my_obj (Object): object to be converted
    Returns:
        JSON representation of object
    """
    return json.dumps(my_obj)
