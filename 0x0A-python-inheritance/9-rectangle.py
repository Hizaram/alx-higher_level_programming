#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
