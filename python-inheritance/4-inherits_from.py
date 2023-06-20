#!/usr/bin/python3
"""the object is an instance of a class that inherited
directly or indirectly from the specified class.
"""


def inherits_from(obj, a_class):
    """ a function that returns True, otherwise False"""
    if isinstance(obj, type) and type(obj) is not a_class:
        return True
    else:
        return False
