#!/usr/bin/python3
"""the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """a function that returns True if the object is exactly
    an instance; otherwise False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
