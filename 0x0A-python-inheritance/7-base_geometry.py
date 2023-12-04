#!/usr/bin/python3
"""BaseGeometry."""


class BaseGeometry():
    """
    BaseGeometry.

    Attributes:
        pass
    """

    def __init__(self):
        """init."""
        pass

    def area(self):
        """Calc area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validat value as int."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return True
