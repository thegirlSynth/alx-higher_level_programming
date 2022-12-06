#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return

    index = 1
    biggest = my_list[0]
    while (index < len(my_list)):
        if my_list[index] >= biggest:
            biggest = my_list[index]
        index += 1

    return biggest
