#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [True for i in range(len(my_list))]
    index = 0

    while (index < len(my_list)):
        if my_list[index] % 2 != 0:
            new_list[index] = False
        index += 1

    return new_list
