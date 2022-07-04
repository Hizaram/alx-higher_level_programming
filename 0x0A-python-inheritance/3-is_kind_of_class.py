#!/usr/bin/python3
"""Function that checks to see if obj is an instance of a_class
or an instance of a class inherited from a_class"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class or an instance
    of a class inherited from a_class
    Args:
        obj (Object): object
        a_class (Object): class to be compared to
    Returns:
         True if it is an instance, False if otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
