#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value."""

    if a_dictionary:
        new_dict = sorted(a_dictionary, key=a_dictionary.get)
        return new_dict[len(a_dictionary) - 1]
