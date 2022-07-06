#!/usr/bin/python3
"""A class Student"""


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
        return (self.__dict__)
