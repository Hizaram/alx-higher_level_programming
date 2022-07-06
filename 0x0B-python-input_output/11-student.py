#!/usr/bin/python3
"""writes a class Student"""


class Student:
    """A Student class"""

    def __init__(self, first_name, last_name, age):
        """__init__ method for class Student
        Args:
            first_name (str): student firstName
            last_name (str): student lastName
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
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

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        Args:
            json (dict): json dict
        """
        for k, v in json.items():
            if hasattr(self, k):
                setattr(self, k, v)
