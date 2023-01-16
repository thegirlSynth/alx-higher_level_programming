#!/usr/bin/python3
"""This module contains a class ``Square``"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This geometry class ``Square`` inherits from ``Rectangle``"""

    def __init__(self, size):
        """This method initializes the class"""
        self.integer_validator('size', size)
        super().__init__(size, size)
