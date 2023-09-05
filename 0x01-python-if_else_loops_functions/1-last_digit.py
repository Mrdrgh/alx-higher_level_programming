#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
neg_number = 0
if number < 0:
    pos_number = -number
else:
    pos_number = number
mod = pos_number % 10
if number < 0:
    mod = -mod
if mod < 6:
    if mod != 0:
        print(f"Last digit of {number} is {mod} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {mod} and is 0")
else:
    print(f"Last digit of {number} is {mod} and is greater than 5")
