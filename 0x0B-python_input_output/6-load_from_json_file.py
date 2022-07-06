#!/usr/bin/python3
"""Function that creates an Object from a json file"""
import json


def load_from_json_file(filename):
    """Creates an object from a json file
    Args:
        filename (str): name of the json file
    Returns:
        Python Object
    """
    Object = None
    with open(filename, 'r', encoding='utf-8') as f:
        Object = json.load(f)
    return Object
