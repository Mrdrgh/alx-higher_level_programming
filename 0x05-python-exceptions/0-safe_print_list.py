#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ret = 0
    for i in my_list:
        try:
            print("{:d}".format(my_list[i]), end = "")
            ret += 1
        except IndexError:
            break
    return (ret)
