#!/usr/bin/python3
"""Function that writes a Python Object to a text file
using JSON string representation"""
import json


def save_to_json_file(my_obj, filename):
    """Writes my_obj to filename using json representation
    Args:
        my_obj (Object): object to be serialized
        filename (str): file to be saved to
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
