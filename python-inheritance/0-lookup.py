#!/usr/bin/python3
def lookup(obj):
    'print(__import__("my_module").my_function.__doc__)'
    return dir(obj)
