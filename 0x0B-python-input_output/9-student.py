#!/usr/bin/python3
"""A class Student"""


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

    def to_json(self):
        """serializes an object"""
        return (self.__dict__)


if __name__ == '__main__':
    students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

    for student in students:
        j_student = student.to_json()
        print(type(j_student))
        print(j_student['first_name'])
        print(type(j_student['first_name']))
        print(j_student['age'])
        print(type(j_student['age']))
