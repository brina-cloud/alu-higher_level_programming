#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy
    for key in new_dict:
        new_dict[key] *= 2
        print("{}: {}".format(key, new_dict[key]))
    return new_dict
