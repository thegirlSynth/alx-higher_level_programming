#!/usr/bin/python3
"""
"""

def add_integer(a, b=98):
    """
    Add two numbers and return the result.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int: The sum of the two numbers.

    Example:
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """

    if isinstance(a, int) or isinstance(a, float):
        if isinstance(b, int) or isinstance(b, float):
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")

