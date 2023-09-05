#!/usr/bin/python3
def print_last_digit(number):
    pos_nbr = 0
    if number < 0:
        pos_nbr = -number
    else:
        pos_nbr = number
    mod = pos_nbr % 10
    print("{}".format(mod), end="")
    return ()
