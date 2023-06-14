#!/usr/bin/python3
"""class Square"""


class Square:
    """Define your square by size (private instance attribute)"""
    def __init__(self, size=0):
        self.__size = size

    """Property def size(self): to retrieve it"""
    @property
    def size(self):
        return self.__size

    """Property setter def size(self, value): to set it"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Returns the current square area"""
    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
