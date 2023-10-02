#!/usr/bin/python3
"""continue"""


class Rectangle:
    """define a rec class"""
    def __init__(self, width=0, height=0):
        """init the rec object with a width of 0
        and a height of 0
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rec
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve the width of the rectangle obj"""
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
        """retrieve the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns the perimiter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """return a string representaion of the rectangle class"""
        if self.__height == 0 or self.__width == 0:
            return ("")

        res = []
        for i in range(self.__height):
            for j in range(self.__width):
                res.append("#")
            if i == self.__height - 1:
                res.append("\n")
        return (res)
