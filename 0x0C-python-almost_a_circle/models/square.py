#!/usr/bin/python3
"""This module contains a class `Square`"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This geometry class inherits from the `Rectangle` class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the `Square` class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the value of the square size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value for square size"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the class attributes"""

        if len(args):
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                if key == 1:
                    self.width = value
                    self.height = value
                if key == 2:
                    self.x = value
                if key == 3:
                    self.y = value

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def __str__(self):
        """Overriding string method for Square class"""
        first_part = ' ({}) {}/{}'.format(self.id, self.x, self.y)
        second_part = ' - {}'.format(self.width)
        return '[Square]' + first_part + second_part

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return dict(id=self.id, size=self.size, x=self.x, y=self.y)
