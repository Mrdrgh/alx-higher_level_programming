#!/usr/bin/python3
"""based on 0 file , we will continue"""


class Rectangle:
    """repr a rectangle"""
    def __init__(self, width=0, height=0):
        """a rectangle class
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rec
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set the value of the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set or get the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
