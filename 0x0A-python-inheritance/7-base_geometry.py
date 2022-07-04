#!/usr/bin/python3
"""a class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry with area() and integer_validator() methods"""
    def area(self):
        """area method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator
        Args:
            name (str): name
            value (int): value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 1
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
