#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = len(sys.argv) - 1
    if s == 0:
        print("{} arguments.".format(s))
    elif s == 1:
        print("{} argument:".format(s))
    else:
        print("{} arguments:".format(s))

    if s >= 1:
        for i in range(1, len(sys.argv)):
                print("{}: {}".format(i, sys.argv[i]))
