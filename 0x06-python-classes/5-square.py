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

    def my_print(self):
        """Prints a representation of the square using `#`"""
        if self.__size != 0:
            for rows in range (0, self.__size):
                print('#' * self.__size)
        else:
            print()
