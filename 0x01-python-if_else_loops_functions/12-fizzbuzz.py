#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3:
            print("{}".format("Fizz"), end="")
        if i % 5:
            print("{}".format("Buzz"), end="")
        if i % 5 != 5 and i % 3 != 0:
            print("{}".format(i), end="")
        if i != 100:
            print("{}".format(" "), end="")
