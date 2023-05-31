#!/usr/bin/python3
import sys
if __name__ == "__main__":

    i = len(sys.argv) - 1
    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(i))
        i = 1
        for arg in sys.argv[1:]:
            print("{}: {}".format(i, arg))
            i += 1
