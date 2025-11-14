#!/usr/bin/python3
"""Module that provides a function to convert objects to json strings"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string"""

    return json.dump(my_obj)
