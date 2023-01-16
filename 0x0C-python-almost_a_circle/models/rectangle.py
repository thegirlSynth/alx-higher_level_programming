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
        self.__width = value

    @property
    def height(self):
        """This returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets the value of height"""
        self.__height = value

    @property
    def x(self):
        """This returns the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """This sets the value of x"""
        self.__x = value

    @property
    def y(self):
        """This returns the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """This sets the value of y"""
        self.__y = value
