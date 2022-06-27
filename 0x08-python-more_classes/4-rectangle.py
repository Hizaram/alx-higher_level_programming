#!/usr/bin/python3
"""A script that creates a class Rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """__init__ method to create a rectangle
        Args:
            width (int): integer width
            height (int): height as an integer
        """
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of rect"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of rect"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    @property
    def width(self):
        """returns the width of rectangle"""
        return self.__width

    @property
    def height(self):
        """returns the height of rect"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter method for width
        Args:
            width (int): the value of width of rectangle
        Raises:
            TypeError: if `width` is not an integer
            ValueError: if `width` is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter method for height
        Args:
            height (int): value for the height of rect
        Raises:
            TypeError: if `height` is not an integer
            ValueError: if `height` is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """Representation of the rectangle with char `#`
        Returns:
            string representation of rectangle
        """
        string = ''
        if self.__width == 0 or self.__height == 0:
            return string
        for r in range(self.__height - 1):
            for c in range(self.__width):
                string += '#'
            string += '\n'
        string += '#' * self.__width
        return string

    def __repr__(self):
        """Representation (str) of Rectangle Object"""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)
