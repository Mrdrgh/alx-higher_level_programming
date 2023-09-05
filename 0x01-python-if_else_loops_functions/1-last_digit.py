#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
neg_number = 0
if number < 0:
    neg_number = -number
else:
    neg_number = number
mod = neg_number % 10
if number < 0:
    mod = -mod
print(number)
print(mod)