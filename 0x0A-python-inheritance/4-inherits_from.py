#!/usr/bin/python3
"""Module that checks if an obj is exactly an instance of
an inherited class"""


def inherits_from(obj, a_class):
    """Function that checks if obj is exactly an instance of
    a class that inherits from a_class
    Args:
        obj (Object): object
        a-class (Object): class to compare to
    Returns:
        True if it matches, False if otherwise
    """
    if issubclass(type(obj), a_class):
        if type(obj) is not a_class:
            return True
    return False
