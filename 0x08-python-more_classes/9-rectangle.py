#!/usr/bin/python3
"""rectangle class."""


class Rectangle:
    """
    rectangle class.

    Attributes:
        __width (int): rectangle size
        __height (int): rectangle size
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init."""
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Cal area."""
        return self.__height * self.__width

    def perimeter(self):
        """Cal perimeter."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Str callback."""
        if self.__height == 0 or self.__width == 0:
            return ""
        r = ""
        for x in range(self.__height):
            r += (str(self.print_symbol) * self.__width) + "\n"
        return r[:-1]

    def __repr__(self):
        """Repr callback."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Del callback."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """Cal biggest area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Cal square."""
        return cls(size, size)
