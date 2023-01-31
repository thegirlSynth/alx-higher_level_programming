#!/usr/bin/python3
"""This module contains a class Square"""


class Square:
    """This is a geometry class"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiates an Instance of Square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the value for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Validates the value to be assigned to size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the value for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Validates the value to be assigned to position"""
        errMsg = "position must be a tuple of 2 positive integers"
        if not isinstance(value, tuple):
            raise TypeError("".format(errMsg))
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("".format(errMsg))
        if value[0] < 0 or value[1] < 0:
            raise TypeError("".format(errMsg))
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints a representation of the square using `#`"""
        print("\n" * self.__position[1], end="")

        if self.__size != 0:
            for rows in range(0, self.__size):
                print(" " * self.__position[0], end="")
                print('#' * self.__size)
        else:
            print()
