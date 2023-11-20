#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    xx = 0

    for i in range(x):
        try:
            print(my_list[i], end='')
            xx += 1
        except IndexError:
            print()
            return xx
    print()
    return xx
