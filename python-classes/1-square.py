#!/usr/bin/python3
"""class Square"""


class Square:
    """Defines a square by size (private instance attribute)"""
    def __init__(self, size):
        self.__size = size

    def size(self):
        return self.__size
