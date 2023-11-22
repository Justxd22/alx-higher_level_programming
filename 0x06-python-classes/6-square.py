#!/usr/bin/python3
"""
square class
"""


class Square:
    """square class
    Attributes:
        __size (int): square size
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square instance.
        """
        if not type(size) is int:
            raise (TypeError("size must be an integer"))
        elif size < 0:
            raise (TypeError("size must be >= 0"))
        self.__size = size
        self.position = position

    def area(self):
        """calc square size instance.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """get size val
        """
        return self.__size

    @property
    def position(self):
        """get position val
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set position val
        """
        e = "position must be a tuple of 2 positive integers"
        if not isinstance(value, tuple) or len(value) != 2:
            raise (TypeError(e))
        elif value[0] < 0 or value[1] < 0:
            raise (TypeError(e))
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise (TypeError(e))
        self.__position = value

    @size.setter
    def size(self, value):
        """set size val
        """
        if not type(value) is int:
            raise (TypeError("size must be an integer"))
        elif value < 0:
            raise (TypeError("size must be >= 0"))
        self.__size = value

    def my_print(self):
        """print a square
        """
        if self.__size == 0:
            return print()
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
