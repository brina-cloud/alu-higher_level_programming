#!/usr/bin/pyhton3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
    except IndexError:
        pass
        print()
        return i
    print()
    return x
