#!/usr/bin/python3
"""A class Base"""
import json


class Base:
    """The Base class of our project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ method for class Base
        Args:
            id (int): id of objects
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
