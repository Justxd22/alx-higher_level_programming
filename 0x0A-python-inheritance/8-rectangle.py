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
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return True


class Rectangle(BaseGeometry):
    """
    Rectangle.

    Attributes:
        inheritates from basegeo
    """

    def __init__(self, width, height):
        """init."""
        if super().integer_validator("width", width):
            self.__width = width
        if super().integer_validator("height", height):
            self.__height = height
