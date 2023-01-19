#!/usr/bin/python3
"""This module contains a class ``Rectangle``"""
from models.base import Base


class Rectangle(Base):
    """This class inherits from the `Base` class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This is a constructor for the `Rectangle` class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets the value of width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """This returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets the value of height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """This returns the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """This sets the value of x"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """This returns the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """This sets the value of y"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Prints the Rectangle instance with the character `#`"""
        for i in range(0, self.__y):
            print()
        for j in range(0, self.__height):
            print(' ' * self.__x, end="")
            for k in range(0, self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """String method for Rectangle class"""
        first_part = ' ({}) {}/{}'.format(self.id, self.__x, self.__y)
        second_part = ' - {}/{}'.format(self.__width, self.__height)
        return '[Rectangle]' + first_part + second_part

    def update(self, *args, **kwargs):
        """Updates the class attributes"""

        if len(args):
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                if key == 1:
                    self.width = value
                if key == 2:
                    self.height = value
                if key == 3:
                    self.x = value
                if key == 4:
                    self.y = value

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        dic = dict(id=self.id, width=self.width, height=self.height, x=self.x)
        dic['y'] = self.y
        return dic
