#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """Class Base : The "base” of all other classes

    Attributes:
        __nb_objects (int): The number of instantiated Bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base

        Args:
            id (int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): A list of instances who inherits of Base
            (ex: list of Rectangle or list of Square instances)
        """
        list_data = []
        if list_objs is None:
            list_data = []
        else:
            list_data = [obj.to_dictionary() for obj in list_objs]

        with open((cls.__name__ + ".json"), "w", encoding='utf-8') as f:
            f.write(cls.to_json_string(list_data))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string

        Args:
            json_string (str): A JSON str representation of a list of dicts
        """
        if json_string is None:
            return []
        return json.loads(json_string)
