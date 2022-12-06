#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for index in range(0, len(my_string)):
        if my_string[index] not in "Cc":
            new_string = new_string + my_string[index]
    return new_string
