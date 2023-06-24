#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function that retrieves a dictionary representation
        of a Student instance"""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
