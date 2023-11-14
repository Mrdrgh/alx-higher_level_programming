#!/usr/bin/python3
"""print what ever"""


def print_square(size):
    """print a square
    Args:
        size (int): the size of the square to print out
    """
    if type(size) is not int or type(size) is not float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="") 
        print("")
