#!/usr/bin/python3
"""Is this Same class?? or not."""


def is_kind_of_class(obj, a_class):
    """
    Is this Same class?? or not.

    Parameters:
    - obj: object to lookup
    - a_class: class to compare
    """
    return isinstance(obj, a_class)
