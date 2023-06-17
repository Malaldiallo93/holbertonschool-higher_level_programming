#!/usr/bin/python3
"""
class Rectangle :
Class that define a rectangle

Args:
    width (int, optional): width of the rectangle. Defaults to 0.
    height (int, optional): height of the rectangle. Defaults to 0.
"""


class Rectangle:
    """Defines a rectangle with width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Print the rectangle with the character #"""
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        for column in range(self.__height):
            for row in range(self.__width):
                str += "#"
            if column is not self.__height - 1:
                str += "\n"
        return str
