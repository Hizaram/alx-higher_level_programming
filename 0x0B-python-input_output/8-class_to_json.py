#!/usr/bin/python3
"""Function that returns the dict description with simple
data structure for JSON serialization"""


def class_to_json(obj):
    """Serializes simple data structures and return their json string
    Args:
        obj (Object): object
    Returns:
        json string
    """
    return (obj.__dict__)
