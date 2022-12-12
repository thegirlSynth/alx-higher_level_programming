#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys."""
    sort_list = sorted(a_dictionary)
    for x in sort_list:
        print("{}: {}".format(x, a_dictionary[x]))
