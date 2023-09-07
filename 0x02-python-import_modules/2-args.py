#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    j = 1
    length = len(sys.argv)
    if length == 1:
        print("{} arguments".format(length - 1))
    elif length == 2:
        print("{} argument".format(length - 1))
    else:
        print("{} arguments:".format(length - 1))
    for i in sys.argv[1:]:
        print("{}: {}".format(j, sys.argv[j]))
        j += 1
