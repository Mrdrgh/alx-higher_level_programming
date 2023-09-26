#!/usr/bin/python3
"""more and more, now with using a setter"""


class Square:
    """ a class of square"""

    def __init(self, size=0):
        """the initialiser
        Args:
            size (int): the size of the square
        """
        self.size = size

    @property
    def size(self):
        """set the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)
