#!/usr/bin/python3
"""class Square"""


class Square:
    """Define your square by size (private instance attribute)"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Returns the current square area"""
    def area(self):
        return self.__size * self.__size
