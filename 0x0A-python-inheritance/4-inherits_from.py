#!/usr/bin/python3
"""Is it inherit?? or not."""


def inherits_from(obj, a_class):
    """
    Is it inherit?? or not.

    Parameters:
    - obj: object to lookup
    - a_class: class to compare
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
