#!/usr/bin/python3
"""This module contains the class MagicClass"""
import dis
import math


class MagicClass:
    """This is a magic geometry class"""

    def __init__(self, radius):
        """This method initiates the instance attributes"""
        self.__radius = 0

        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the MagicClass"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference of the MagicClass"""
        return 2 * math.pi * self.__radius


if __name__ == "__main__":
    dis.dis(MagicClass)
