#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j == 9 and i == 8:
            print("{}{}".format(i, j))
        elif i * 10 + j < j * 10 + i:
            print("{}{}, ".format(i, j), end="")
