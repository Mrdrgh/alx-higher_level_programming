#!/usr/bin/python3
"""the base file """


class Base:
    """the base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """the constructor
        Args:
            id (any): the id of the base obj
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects 
