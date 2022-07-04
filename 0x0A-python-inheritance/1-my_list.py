#!/usr/bin/python3
"""A module that creates a class MyList"""


class MyList(list):
    """Class MyList that inherits from the superclass list"""
    def print_sorted(self):
        """Sorts a list using any sorting method
        Args: unsorted list
        Returns: sorted list
        """
        print(sorted(self))
