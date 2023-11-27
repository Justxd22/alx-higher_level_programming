#!/usr/bin/python3
"""rectangle class."""


class Rectangle:
    """
    rectangle class.

    Attributes:
        __width (int): rectangle size
        __height (int): rectangle size
    """

    def __init__(self, width=0, height=0):
        """init."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get width val."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width val."""
        if not type(value) is int:
            raise (TypeError("width must be an integer"))
        elif value < 0:
            raise (TypeError("width must be >= 0"))
        self.__width = value

    @property
    def height(self):
        """Get height val."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height val."""
        if not type(value) is int:
            raise (TypeError("height must be an integer"))
        elif value < 0:
            raise (TypeError("height must be >= 0"))
        self.__height = value
