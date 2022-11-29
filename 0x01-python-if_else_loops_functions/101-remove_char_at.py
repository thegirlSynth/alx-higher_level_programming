#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    number = 0

    for i in str:
        number += 1

    if n < number and n >= 0:
        for i in str:
            if i != str[n]:
                newstr += i
    else:
        newstr = str
    return(newstr)
