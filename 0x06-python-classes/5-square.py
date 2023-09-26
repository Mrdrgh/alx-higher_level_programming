#!/usr/bin/python3
"""more and more"""


class Square:
    """The square class"""

    def __init__(self, size=0):
        """init the size attr
        Args:
            size (int): the size of the square
        """
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value=0):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("{}".format("#"), end="")
            print("")
        if self.__size == 0:
            print("")
