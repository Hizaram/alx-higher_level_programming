#!/usr/bin/python3
"""A module that creates a class MyList"""


class MyList(list):
    """Class MyList that inherits from the superclass list"""
    def print_sorted(self):
        """Sorts a list using any sorting method
        Args: unsorted list
        Returns: sorted list
        """
        array = self[:]
        isDone = False

        while not isDone:
            isDone = True
            for i in range(len(array)-1):
                if array[i] > array[i+1]:
                    arrray[i], array[i+1] = array[i+1], array[i]
                    isDone = False
        print(array)
