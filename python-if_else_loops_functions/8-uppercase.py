#!/usr/bin/python3
def uppercase(str):
    for u in str:
        if 'a' <= u <= 'z':
           u = chr(ord(u) - 32)
           print("{}".format(u), end="")
    print()
