#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square : Inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square

        Args:
            id (int): The identity of the new Square
            size (int): The size of the new Square
            x (int): The x coordinate of the new Square
            y (int): The y coordinate of the new Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size = width = height"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size = width = height"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square

        Args:
            *args (ints): New attribute values
                In order : id, size, x, y
            **kwargs (dict):
                1st argument = id attribute
                2nd argument = size attribute
                3rd argument = x attribute
                4th argument = y attribute
        """
        if args is not None and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "size":
                    self.size = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {"x": self.x, "y": self.y, "id": self.id, "size": self.height}

    def __str__(self):
        """Return description of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
