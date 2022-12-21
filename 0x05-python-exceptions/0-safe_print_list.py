#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        index = 0
        while index < x:
            print(my_list[index], end="")
            index = index + 1
        print()
        return (index)

    except IndexError:
        print()
        return (index)
