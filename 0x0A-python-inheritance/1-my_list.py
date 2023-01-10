#!/usr/bin/python3
"""This module contains the class `MyList`"""


class MyList(list):
    """This class inherits from the `list` class"""

    def print_sorted(self):
        """Prints the list in sorted, ascending order"""
        print(sorted(self))
