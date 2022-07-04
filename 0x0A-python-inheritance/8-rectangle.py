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
