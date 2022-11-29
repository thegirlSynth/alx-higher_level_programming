#!/usr/bin/python3
for character in range(ord('z'), ord('a')-1, -1):
    if character % 2 != 0:
        character -= 32
    print("{}".format(chr(character)), end="")
