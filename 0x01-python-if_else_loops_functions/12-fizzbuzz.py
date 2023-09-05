#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("{}".format("Fizz"), end="")
        if i % 5 == 0:
            print("{}".format("Buzz"), end="")
        print("{}".format(' '), end="")
        if i % 3 != 0 and i % 5 != 0:
            if i != 100:
                print("{} ".format(i), end="")
                print("{}".format(' '), end="")
            else:
                print("{}".format(i))
                print("{}".format(' '), end="")
