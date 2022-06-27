#!/usr/bin/python3
"""A script that creates a class Rectangle"""


class Rectangle:
    """Rectangle class
    Attributes:
        number_of_instances (int): counter that increments when rect
        is initialised and decrements when it is deleted
        print_symbol (any_type): character(s) to represent Rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """__init__ method to create a rectangle
        Args:
            width (int): integer width
            height (int): height as an integer
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
                string += str(self.print_symbol)
            string += '\n'
        string += str(self.print_symbol) * self.__width
        return string

    def __repr__(self):
        """Representation (str) of Rectangle Object"""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        """Method upon when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle among two instances
        Args:
            rect_1 (Rectangle): Rectangle instance 1
            rect_2 (Rectangle): Rectangle instance 2
        Raises:
            TypeError: if any of the rectangles isnt an instance if Rectangle
        Returns:
            Bigger rectangle, returns rect_1 if both are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
