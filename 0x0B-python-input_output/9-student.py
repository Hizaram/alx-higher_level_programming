#!/usr/bin/python3
"""A class Student"""


def class_to_json(obj):
    """Serializes simple data structures and return their json string
    Args:
        obj (Object): object
    Returns:
        json string
    """
    return (obj.__dict__)


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

    def to_json(self):
        """serializes an object"""
        return class_to_json(self)
