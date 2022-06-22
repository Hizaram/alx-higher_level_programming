#!/usr/bin/python3
"""Script that creates a class Square"""


class Square:
    """a class Square"""

    def __init__(self, size=0):
        """__init__ method that sets the size of square
        Args:
            size (int): size of Square

        """
        self.__size = size

    def area(self):
        """Tasked at getting the area of square

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
        """size setter that sets size based on value
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


if __name__ == '__main__':
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
