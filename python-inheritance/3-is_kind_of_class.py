#!/usr/bin/python3
"""the object is an instance of, or if the object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """function that returns True, otherwise False. """
    if isinstance(obj, a_class):
        return True
    else:
        return False
