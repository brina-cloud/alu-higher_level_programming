#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    new_in_list = my_list.copy()
    if idx < 0:
        return new_in_list
    elif idx >= len(my_list):
        return new_in_list
    else:
        new_in_list[idx] = new_element
    return new_in_list
