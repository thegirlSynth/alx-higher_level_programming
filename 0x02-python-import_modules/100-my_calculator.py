#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, op, b = argv[1], argv[2], argv[3]

    if op not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    else:
        if op == "+":
            print("{} {} {} = {}".format(a, op, b, add(int(a), int(b))))
        if op == "-":
            print("{} {} {} = {}".format(a, op, b, sub(int(a), int(b))))
        if op == "*":
            print("{} {} {} = {}".format(a, op, b, mul(int(a), int(b))))
        if op == "/":
            print("{} {} {} = {}".format(a, op, b, div(int(a), int(b))))
