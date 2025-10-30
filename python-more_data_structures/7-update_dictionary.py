#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = a_dictionary.copy()
    a_dictionary[key] = value
    return a_dictionary
    for key, value in a_dictionary.items():
        print("{}: {}".format(key, value))
