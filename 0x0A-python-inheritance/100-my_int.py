#!/usr/bin/python3
"""MyInt."""


class MyInt(int):
    """MyInt."""

    def __init__(self, value):
        """init."""
        self.value = value

    def __eq__(self, b):
        """Reverse equal."""
        return self.value != b

    def __ne__(self, b):
        """Reversr not equal."""
        return self.value == b
