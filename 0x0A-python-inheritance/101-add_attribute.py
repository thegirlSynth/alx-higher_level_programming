#!/usr/bin/python3
"""This module contains a function `add_attribute`"""


def add_attribute(object, name, value):
    """This method adds an attribute to an object if it is possible"""

    if hasattr(object, '__dict__'):
        setattr(object, name, value)

    else:
        raise TypeError("can't add new attribute")
