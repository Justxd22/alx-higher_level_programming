#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not a_dictionary:
        return
    added = 0
    for x in a_dictionary:
        if x == key:
            a_dictionary[x] = value
            added = True
    if not added:
        a_dictionary[key] = value
    return a_dictionary
