#!/usr/bin/python3
"""rectangle py"""


class Rectangle(Base):
    """ a class of an rectangle object""" 

    @property
    def width(self):
        """get/set the width of the rec"""
        return self.__width
    
    @width.setter
    def width(self, value):
        self.__width = value
    
    @property
    def height(self):
        return (self.__height) 
    
    @height.setter
    def height(self, value):
        self.__height = value
    @property
    def x(self):
        return (self.__x)
    
    @x.setter
    def x(self, value):
        self.__x

    @property
    def y(self):
        return (self.__y)
    
    @y.setter
    def y(self, value):
        self.__y = value
    
