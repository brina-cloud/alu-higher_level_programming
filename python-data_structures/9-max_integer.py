#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max_integer = my_list[0]
        for value in my_list[1:]:
            if value > max_integer:
               max_integer = value
        return max_integer
