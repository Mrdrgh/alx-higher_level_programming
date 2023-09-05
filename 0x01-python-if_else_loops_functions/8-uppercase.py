#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i > 97 and i < 97 + 26:
            i = i - 32
            print("{}".format(i), end="")
    print(end="\n")
