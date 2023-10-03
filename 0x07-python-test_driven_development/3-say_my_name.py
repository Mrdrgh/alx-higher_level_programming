#!/usr/bin/python3
"""the python file number 3"""


def say_my_name(first_name, last_name=""):
    """print a name
    Args:
        first_name (str): the first name
        last_name (str): the last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("Py name is {} {}".format(first_name, last_name))
