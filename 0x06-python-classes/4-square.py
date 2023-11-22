#!/usr/bin/python3
"""
square class
"""


class Square:
    """square class
    Attributes:
        __size (int): square size
    """
    def __init__(self, size=0):
        """Initialize the square instance.
        """
        if not type(size) is int:
            raise (TypeError("size must be an integer"))
        elif size < 0:
            raise (TypeError("size must be >= 0"))
        self.__size = size

    def area(self):
        """calc square size instance.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """get size val
        """
        return self.__size

    @size.setter
    def size(self, value=None):
        """set size val
        """
        if not type(value) is int:
            raise (TypeError("size must be an integer"))
        elif value < 0:
            raise (TypeError("size must be >= 0"))
        self.__size = value
