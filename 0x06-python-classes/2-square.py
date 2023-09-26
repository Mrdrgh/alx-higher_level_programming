#!/usr/bin/python3
"""more on the classes"""


class Square():
    """define a square class with a private attr (size)
    Args:
        size (int): the size of the square class
    """
    def __init__(self, size=0):
        self.__size = size
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
