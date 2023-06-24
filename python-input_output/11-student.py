#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """Class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function that retrieves a dictionary representation
        of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {key: self.__dict__[key] for key in self.__dict__
                        if key in attrs}
            return new_dict

    def reload_from_json(self, json):
        """Function that that replaces all attributes
        of the Student instance"""
        for key in json:
            if key in self.__dict__:
                self.__dict__[key] = json[key]
