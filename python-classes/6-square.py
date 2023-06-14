#!/usr/bin/python3
"""class Square"""


class Square:
    """Define your square by size (private instance attribute)"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    """Property def position(self): to retrieve it"""
    @property
    def position(self):
        return self.__position

    """Property setter def position(self, value): to set it"""
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """Returns the current square area"""
    def area(self):
        return self.size * self.__size

    """Prints in stdout the square with the character #"""
    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
