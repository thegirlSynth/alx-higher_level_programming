#!/usr/bin/python3
"""This module contains a class Square"""


class Square:
    """This is a geometry class"""
    def __init__(self, size=0):
        """Instantiates an Instance of Square"""
        self.size = size

    @property
    def size(self):
        """Returns the value for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Validates the valie to be assigned to size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __eq__(self, object):
        """Defines the == comparison of the square area"""
        return self.area() == object.area()

    def __ne__(self, object):
        """Defines the != comparison of the square area"""
        return self.area() != object.area()

    def __lt__(self, object):
        """Defines the < comparison of the square area"""
        return self.area() < object.area()

    def __le__(self, object):
        """Defines the <= comparison of the square area"""
        return self.area() <= object.area()

    def __gt__(self, object):
        """Defines the < comparison of the square area"""
        return self.area() > object.area()

    def __ge__(self, object):
        """Defines the <= comparison of the square area"""
        return self.area() >= object.area()
