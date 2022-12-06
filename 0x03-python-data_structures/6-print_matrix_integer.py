#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for number in item:
            if item.index(number) == 0:
                print("{:d}".format(number), end="")
            else:
                print(" {:d}".format(number), end="")
        print()
