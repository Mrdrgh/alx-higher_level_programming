#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == 0:
            print("{}, ".format("Fizz"), end="")
        if i % 5 == 0:
            print("{}, ".format("Buzz"), end="")
        if i % 3 != 0 and i % 5 != 0:
            if i != 99:
                print("{}, ".format(i))
            else:
                print("{}".format(i))
