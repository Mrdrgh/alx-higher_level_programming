#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    try:
        print("{:d}".format(my_list[x]))
        return (True)
    except (TypeError, ValueError):
        return (False)
