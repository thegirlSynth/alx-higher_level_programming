#!/usr/bin/python3
"""This module contains a class Square"""


class Square:
    """This is a geometry class"""
    def __init__(self, size=0):
        """Instantiates an Instance of Square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
