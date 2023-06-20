#!/usr/bin/python3
"""Class BaseGeometry"""


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
