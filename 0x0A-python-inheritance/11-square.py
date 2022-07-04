#!/usr/bin/python3
"""a class Square that inherits from superclass Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square"""

    def __init__(self, size):
        """__init__ method
        Args:
            size (int): size of square
        Raises:
            same exceptions as superclass
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area method that returns area of square"""
        return self.__size ** 2

    def __str__(self):
        """String representation of square"""
        return "[{}] {:d}/{:d}".format(
            type(self).__name__, self.__size, self.__size)
