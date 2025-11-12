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

    def area(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        return self.__width * self.__height

    def __str__(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        return f"[Rectangle] {self.__width}/{self.__height}"
