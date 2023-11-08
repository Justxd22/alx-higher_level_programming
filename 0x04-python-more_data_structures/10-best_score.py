#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    key = list(a_dictionary.keys())[0]
    for x in a_dictionary:
        if a_dictionary[key] < a_dictionary[x]:
            key = x
    return key
