#!/usr/bin/python3
"""This module contains a function `complex_delete`"""


def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in the dictionary
    """

    del_list = []
    for k, v in a_dictionary.items():
        if v == value:
            del_list.append(k)
    for key in del_list:
        del a_dictionary[key]
    return a_dictionary
