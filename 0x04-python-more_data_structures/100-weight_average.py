#!/usr/bin/python3
"""Returns the weighted average of all integers tuple (<score>, <weight>)"""


def weight_average(my_list=[]):
    if my_list:
        mul = sum(map(lambda item: item[0]*item[1], my_list))
        add = sum(map(lambda item: item[1], my_list))
        return mul/add
    else:
        return 0
