#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""

    def __init__(self, size):
       self.__size = size
       self.integer_validator("size", size)
       super().__init__(size, size)
    def area(self):
       """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
       return self.__size * self.__size
