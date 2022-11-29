#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for c in str:
        if ord(c) in range(ord('a'), ord('z')+1):
            newstr = newstr + chr(ord(c)-32)
        else:
            newstr = newstr + c
    print("{}".format(newstr))
