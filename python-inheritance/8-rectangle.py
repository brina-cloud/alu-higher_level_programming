#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """python3 -c 'print(__import__("my_module").__doc__)'"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
