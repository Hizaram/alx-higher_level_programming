#!/usr/bin/python3
"""Script that creates a class Square"""


class Square:
    """a class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """__init__ method that sets the size and position of a square

        Args:
            size (int): size of square
            position (tuple): position of square

        """
        self.size = size
        self.position = position

    def area(self):
        """Tasked with getting the area of Square
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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter that sets the position of square
        Args:
            value (tuple): tuple of two, positive integer coordinates
        Raises:
            TypeError: if `value` is not tuple of 2 positive int coordinates

        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Prints a # representation of square based on size."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(' ' * self.__position[0], end='')
                print("#" * self.__size)
