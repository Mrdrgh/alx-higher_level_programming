#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first_arg = 0
    second_arg = 0
    if isinstance(tuple_a, tuple) and len(tuple_a) == 2:
        first_arg += tuple_a[0]
        second_arg += tuple_a[1]
    if isinstance(tuple_b, tuple) and len(tuple_b) == 2:
        first_arg += tuple_b[0]
        second_arg += tuple_b[1]
    res = first_arg, second_arg
    return (res)
