#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if not a_dictionary:
        return
    z = {}
    for x in a_dictionary:
        z[x] = a_dictionary[x] * 2
    return z
