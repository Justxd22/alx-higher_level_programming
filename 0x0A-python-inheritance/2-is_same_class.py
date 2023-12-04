#!/usr/bin/python3
"""Is this Same class?? or not."""


def is_same_class(obj, a_class):
    """
    Is this Same class?? or not.

    Parameters:
    - obj: object to lookup
    - a_class: class to compare
    """
    return a_class is type(obj)
