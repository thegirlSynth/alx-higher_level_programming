#!/usr/bin/python3
"""This module contains a class ``Base``"""


class Base:
    """This class is the base class for the module"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
