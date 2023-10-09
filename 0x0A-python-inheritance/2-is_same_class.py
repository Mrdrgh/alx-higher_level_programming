#!/usr/bin/python3
"""return true if the instance is the same type of a class"""


def is_same_class(obj, a_class):
    """as written above
    Args:
        obj (any): the object
        a_class(type): the class to check
    Returns:
        true if the same type , false otherwise
    """
    if type(obj) is a_class:
        return (True)
    return (False)
