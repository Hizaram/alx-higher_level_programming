#!/usr/bin/python3


class Square:
    """a class Square"""

    def __init__(self, size=0):
        """__init__ method that sets the size of square
        Args:
            size (int): size of Square

        """
        self.size = size

    def area(self):
        """Tasked at getting the area of square

        Returns:
            Area of square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """returns size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter that sets size based on value
        Args:
            value (int): value of size of square

        Raises:
            TypeError: if `size` is not an integer
            ValueError: if `size` is less than zero

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
