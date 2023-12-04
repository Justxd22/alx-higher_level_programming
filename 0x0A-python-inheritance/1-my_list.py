#!/usr/bin/python3
"""MyList."""


class MyList(list):
    """
    MyList class.

    Attributes:
        list
    """

    def __init__(self):
        """init."""
        pass

    def print_sorted(self):
        """Print in sorted order."""
        print(sorted(self))
