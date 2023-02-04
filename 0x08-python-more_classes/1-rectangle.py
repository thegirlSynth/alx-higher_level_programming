#!/usr/bin/python3
"""This module contains a class Rectangle"""


class Rectangle:
    """Defines a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialises an instance of Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the value for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the value for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
