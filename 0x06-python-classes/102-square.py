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

    def __eq__(self, other):
        """Override the equality comparison.

        Args:
            other (Square): The square to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.

        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Override the not equal comparison.

        Args:
            other (Square): The square to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.

        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Override the less than comparison.

        Args:
            other (Square): The square to compare.

        Returns:
            bool: True if the area is less than the other, False otherwise.

        """
        return self.area() < other.area()

    def __le__(self, other):
        """Override the less than or equal comparison.

        Args:
            other (Square): The square to compare.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Override the greater than comparison.

        Args:
            other (Square): The square to compare.

        Returns:
            bool: True if the area is greater than the other, False otherwise.

        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Override the greater than or equal comparison.

        Args:
            other (Square): The square to compare.
        """
        return self.area() >= other.area()
