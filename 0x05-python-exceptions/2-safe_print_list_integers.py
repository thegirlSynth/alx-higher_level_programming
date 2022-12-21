#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count, index = 0, 0

    while index < x:
        try:
            if (int(my_list[index])):
                print("{:d}".format(my_list[index]), end="")
            index = index + 1
            count = count + 1

        except (TypeError, ValueError):
            index = index + 1
            continue

    print()
    return count
