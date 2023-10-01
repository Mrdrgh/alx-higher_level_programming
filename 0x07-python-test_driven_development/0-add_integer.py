#!/usr/bin/python3
"""add the ints or the  floats"""


def add_integer(a, b=98):
    sum = 0
    try:
        sum += a
    except (TypeError):
        raise TypeError("a must be an integer")
    try:
        sum += b
    except (TypeError):
        raise TypeError("b must be an integer")
    return (sum)
