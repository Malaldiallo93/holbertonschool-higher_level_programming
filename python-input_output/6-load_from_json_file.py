#!/usr/bin/python3
"""JSON file"""


import json


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”:"""
    with open(filename) as json_file:
        json_data = json.load(json_file)
    return json_data
