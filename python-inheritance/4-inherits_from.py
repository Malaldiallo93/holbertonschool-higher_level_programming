#!/usr/bin/python3
"""the object is an instance of a class that inherited
directly or indirectly
"""


def inherits_from(obj, a_class):
    """ a function that returns True, otherwise False"""
    if isinstance(obj, type):
        return True
    else:
        return False
