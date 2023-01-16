#!/usr/bin/python3
"""This module contains a class ``MyInt``"""


class MyInt(int):
    """MyInt inherits from int but it is a rebel.
    It has the == and != operators inverted.
    """

    def __init__(self, value):
        """Initializes  the MyInt class"""
        super().__init__()

    def __ne__(self, object):
        """Returns the value for the != comparison"""
        return super().__eq__(object)

    def __eq__(self, object):
        """Returns the value for the == comparison"""
        return super().__ne__(object)
