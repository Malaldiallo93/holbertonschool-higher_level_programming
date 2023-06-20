#!/usr/bin/python3
"""class Square: subclass that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square, subclass of Rectangle

    comment:
        size (int): size of the square
    """
    def __init__(self, size):
        """Instantiation using Rectangle(subclass) function"""
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Return description of the rectangle/square"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
