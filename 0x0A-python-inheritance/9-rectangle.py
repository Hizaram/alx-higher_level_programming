#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""


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


class Rectangle(BaseGeometry):
    """a class Rectangle"""
    def __init__(self, width, height):
        """__init__ method
        Args:
            width (int) = width of rectangle
            height (int) = height of rectangle
        Raises:
            Same exceptions as contained in the super class
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """string representation of rectangle"""
        return "[{}] {:d}/{:d}".format(
                type(self).__name__, self.__width, self.__height)

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height
