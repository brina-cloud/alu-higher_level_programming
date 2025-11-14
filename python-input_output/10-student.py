#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """A class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance."""
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
