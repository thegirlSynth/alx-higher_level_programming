#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []
    for item in my_list:
        if item != search:
            newlist.append(item)
        else:
            newlist.append(replace)

    return newlist
