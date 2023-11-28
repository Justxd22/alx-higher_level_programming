#!/usr/bin/python3
"""Add Function."""


def add_integer(a, b=98):
    """
    Add two vars.

    Parameters:
    - a (int or float): The first integer or float.
    - b (int or float, default: 98): The second integer or float.
    """
    if not isinstance(a, (float, int)):
        return TypeError("a must be an integer")
    elif not isinstance(b, (float, int)):
        return TypeError("b must be an integer")
    return int(a) + int(b)
