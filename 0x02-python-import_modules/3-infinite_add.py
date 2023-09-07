#!/usr/bin/python3
import sys
if len(sys.argv) <= 1:
    sys.exit()
sum = 0
for i in sys.argv[1:]:
    sum += int(i)
print("{}".format(sum))