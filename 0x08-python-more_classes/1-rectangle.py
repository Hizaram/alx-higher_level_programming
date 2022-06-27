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
        self.width = width
        self.height = height

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


if __name__ == '__main__':
    my_rectangle = Rectangle(-2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
