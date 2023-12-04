#!/usr/bin/python3
"""Lookup."""


def lookup(obj):
    """
    Look up attributes and methods.

    Parameters:
    - obj: object to lookup
    """
    return [ob for ob in dir(obj)]
