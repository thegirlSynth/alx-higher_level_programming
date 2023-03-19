#!/usr/bin/python3
"""This module contains a function `append_write`"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8)
    and returns the number of characters written
    """

    with open(filename, "a", encoding="utf8") as f:
        return f.write(text)
