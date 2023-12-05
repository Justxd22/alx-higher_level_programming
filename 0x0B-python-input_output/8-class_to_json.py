#!/usr/bin/python3
"""ClassToJson."""


def class_to_json(obj):
    """
    Return the dict.

    Parameters:
    - obj: Class

    Returns:
    - Dict
    """
    return obj.__dict__
