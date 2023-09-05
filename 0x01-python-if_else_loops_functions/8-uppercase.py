#!/usr/bin/python3
def uppercase(str):
    res = ""
    for i in str:
        if ord(i) >= 97 and ord(i) < 97 + 26:
            i = chr(ord(i) - 32)
        res += i
    print("{}".format(res))
