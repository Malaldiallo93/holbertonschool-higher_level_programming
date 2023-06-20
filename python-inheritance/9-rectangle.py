#!/usr/bin/python3
"""class Rectangle: subclass that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle, subclass of BaseGeometry

    comments:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """
    def __init__(self, width, height):
        """Instantiation using BaseGeometry(superclass) function"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return description of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height
