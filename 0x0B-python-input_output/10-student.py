#!/usr/bin/python3
"""writes a class Student"""


class Student:
    """A Student class"""

    def __init__(self, firstname, lastname, age):
        """__init__ method for class Student
        Args:
            first_name (str): student firstName
            last_name (str): student lastName
            age (int): age of student
        """
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def to_json(self, attrs=None):
        """Serializes an object
        Args:
            attrs (list): list of attributes to filter object
        Returns:
            Object Dictionary
        """
        obj_dict = self.__dict__
        if not attrs:
            return obj_dict
        else:
            filter_dict = {}
            for attribute in attrs:
                if hasattr(self, attribute):
                    filter_dict[attribute] = obj_dict[attribute]
            return filter_dict
