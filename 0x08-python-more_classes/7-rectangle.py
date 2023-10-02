#!/usr/bin/python3
"""defines a rectangle class."""


class rectangle:
    """represent a rectangle.

    attributes:
        number_of_instances (int): the number of rectangle instances.
        print_symbol (any): the symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize a new rectangle.

        args:
            width (int): the width of the new rectangle.
            height (int): the height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise typeerror("width must be an integer")
        if value < 0:
            raise valueerror("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise typeerror("height must be an integer")
        if value < 0:
            raise valueerror("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """return the printable representation of the rectangle.

        represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """return the string representation of the rectangle."""
        rect = "rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """print a message for every deletion of a rectangle."""
        type(self).number_of_instances -= 1
        print("bye rectangle...")
