#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return
    copy_dict = a_dictionary.copy()
    for key, val in copy_dict.items():
        if value == val:
            del a_dictionary[key]
    return a_dictionary
