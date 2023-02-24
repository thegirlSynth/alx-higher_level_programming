#!/usr/bin/python3
"""This module contains a class Rectangle"""


class Rectangle:
    """Defines a Rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialises an instance of Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Returns the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the Rectangle"""
        if self.__width != 0 and self.__height != 0:
            return 2 * (self.__width + self.__height)
        return 0

    def __str__(self):
        """Prints the Rectangle using the print_symbol attribute"""
        if self.__height != 0 and self.__width != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    print(str(self.print_symbol), end="")
                    j += 1
                if i != self.__height - 1:
                    print()
                i += 1
        return ""

    def __repr__(self):
        """Returns string representation of the rectangle to be able
        to recreate a new instance by using eval()
        """

        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
