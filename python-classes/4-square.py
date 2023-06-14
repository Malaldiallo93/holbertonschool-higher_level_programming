#!/usr/bin/python3
"""class Square"""


class Square:
    """Define your square by size (private instance attribute)"""

    def __init__(self, size=0):
        self.__size = 0
        self.size = size

    """Property def size(self): to retrieve it"""
    def size(self):
        return self.__size

    """Property setter def size(self, value): to set it"""
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Returns the current square area"""
    def area(self):
        return self.__size * self.__size
