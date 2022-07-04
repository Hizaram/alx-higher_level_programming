#!/usr/bin/python3
"""A function that checks to see if obj is exactly an instance of a_class"""


def is_same_class(obj, a_class):
    """Function that checks if obj is exactly an instance of the a_class
    Args:
        obj (Object): object
        a_class (Object): class to compare to
    Returns:
        True if same, False otherwise
    """
    if type(obj).__name__ == a_class.__name__:
        return True
    return False
