#!/usr/bin/python3
"""a class BaseGeometry"""


class BaseGeometry:
    """a class BaseGeometry that raises an exception"""
    def area(self):
        """raises an exception if not implemented"""
        raise Exception("area() is not implemented")
