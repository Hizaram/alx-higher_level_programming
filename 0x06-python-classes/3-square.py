#!/usr/bin/python3


class Square:
    """a class Square"""

    def __init__(self, size=0):
        """__init__ method that defines a Square with size
        Args:
            size (int): size of class Square

        Raises:
            TypeError: if `size` is not an integer
            ValueError: if `size` is less than zero

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Tasked with getting the area of Square

        Return:
            Area of Square
        """
        return self.__size * self.__size
