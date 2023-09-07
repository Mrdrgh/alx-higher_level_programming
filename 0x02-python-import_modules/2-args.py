#!/usr/bin/python3
import sys
print("{} arguments:".format(len(sys.argv) - 1))
j = 1
for i in sys.argv:
    if j == len(sys.argv):
        break
    print("{}: {}".format(j, sys.argv[j]))
    j += 1
