#!/usr/bin/python3


class Square:
    """Square class"""

    def __init__(self, size):
        """__init__ method that sets the size of square
        Args:
            size (int): size of square

        """
        self.size = size

    def area(self):
        """Gets the area of square
        Returns:
            Area of square

        """
        return self.__size * self.__size

    @property
    def size(self):
        """Returns the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method that sets the size of square to value

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

    def my_print(self):
        """Prints the stdout the # representation of square based on size"""
        for r in range(self.__size):
            for c in range(self.__size):
                print("#", end='')
            print()
        if self.__size == 0:
            print()
