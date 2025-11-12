#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class BaseGeometry:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
