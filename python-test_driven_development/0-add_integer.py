#!/usr/bin/python3
"""Module that adds 2 integers and return the sum
    Args:
        a (int):  integers or floats
        b (int):  integers or floats
"""


def add_integer(a, b=98):
    """Function that add two integers or float
    and return the sum.
    """
    try:
        if type(a) is not int and type(a) is not float:
            raise TypeError("a must be an integer")
        if type(b) is not int and type(b) is not float:
            raise TypeError("b must be an integer")
        a = int(a)
        b = int(b)
        return a + b
    except Exception as e:
        return e
