#!/usr/bin/python3
"""This module contains the function `add_integer`"""


def add_integer(a, b=98):
    """This function adds two integers.

    Args:
        a(int/float) - the first integer
        b(int/float) - the second integer

    Returns:
        the sum of a and b, raises an exception otherwise
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return a + b
