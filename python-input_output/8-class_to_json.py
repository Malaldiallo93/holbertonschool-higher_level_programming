#!/usr/bin/python3
"""JSON serialization"""


def class_to_json(obj):
    """A function that returns the dictionary
    description with simple data structure
    """
    json_dict = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
    return json_dict
