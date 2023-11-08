#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return
    for x, a in sorted(a_dictionary.items()):
        print("{}: {}".format(x, a))
