#!/usr/bin/python3
"""Add new attribute."""


def add_attribute(obj, attr, value):
    """Add new attribute."""
    if ("__dict__" not in dir(obj) or "__slots__" in dir(obj) or
       hasattr(obj, attr)):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
