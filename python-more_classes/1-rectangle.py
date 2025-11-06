#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class Rectangle:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            isinstance(value, int)
        except TypeError:
         print("width must be an integer")
        try:
            value >= 0
        except ValueError:
            print("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        try:
            isinstance(value, int)
        except TypeError:
         print("height must be an integer")
        try:
            value >= 0
        except ValueError:
            print("height must be >= 0")
        self.__height = value
