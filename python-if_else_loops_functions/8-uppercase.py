#!/usr/bin/python3
def uppercase(str):
    for u in str:
            print("{}".format(chr(ord(u) - 32) if 'a' <= u <= 'z' else u), end="")
    print()
