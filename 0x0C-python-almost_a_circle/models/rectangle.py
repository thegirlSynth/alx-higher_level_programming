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
