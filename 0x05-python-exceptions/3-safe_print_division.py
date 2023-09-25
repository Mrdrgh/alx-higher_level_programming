#!/usr/bin/python3
def safe_print_division(a, b):
    div = a / b
    try:
        print("{:d}".format(div))
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
