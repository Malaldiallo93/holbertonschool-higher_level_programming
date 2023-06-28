#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle : Inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Base

        Args:
            id (int): The identity of the new Rectangle
            width (int): The width of the new Rectangle
            height (int): The height of the new Rectangle
            x (int): The x coordinate of the new Rectangle
            y (int): The y coordinate of the new Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for heigth"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        print(("\n") * self.__y, end="")
        for column in range(self.__height):
            print((" ") * self.__x, end="")
            for row in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Update the Rectangle

        Args:
            *args (ints): New attribute values
                In order : id, width, height, x, y
            **kwargs (dict):
                1st argument = id attribute
                2nd argument = width attribute
                3rd argument = height attribute
                4th argument = x attribute
                5th argument = y attribute
        """
        if args is not None and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "width":
                    self.width = kwargs[key]
                if key == "height":
                    self.height = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}

    def __str__(self):
        """Return description of the rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}\
 - {self.width}/{self.height}"
 