#!/usr/bin/python3
"""A module that returns the list of available attributes and methods"""


def lookup(obj):
    """Function that returns list of available attr and methods
    Args;
        obj (Object): object
    Returns: list Object
    """
    return dir(obj)
