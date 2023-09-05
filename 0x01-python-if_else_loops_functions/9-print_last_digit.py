#!/usr/bin/python3
def c_mod(a, b):
    return a - b * int(a / b)
def print_last_digit(number):
    print("{}".format(c_mod(number, 10)), end="")
    return (c_mod(number, 10))
