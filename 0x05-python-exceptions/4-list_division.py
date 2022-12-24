#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    index = 0
    while index < list_length:
        try:
            result = my_list_1[index] / my_list_2[index]
            new_list = new_list + [result]

        except ZeroDivisionError:
            print("division by 0")
            new_list = new_list + [0]

        except TypeError:
            print("wrong type")
            new_list = new_list + [0]

        except IndexError:
            print("out of range")
            new_list = new_list + [0]

        finally:
            index = index + 1

    return new_list
