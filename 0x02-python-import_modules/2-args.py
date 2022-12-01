#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{}".format((len(argv) - 1)), end="")
    if len(argv) == 1:
        print(" arguments.")
    if len(argv) > 2:
        print(" arguments:")
    if len(argv) == 2:
        print(" argument:")

    for item in argv:
        if argv.index(item) > 0:
            print("{}: {}".format(argv.index(item), item))
