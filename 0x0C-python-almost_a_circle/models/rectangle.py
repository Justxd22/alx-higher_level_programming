#!/usr/bin/python3
"""Rectangle."""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle.

    Attributes:
        Base Class
    """

    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width."""
        if not type(value) is int:
            raise (TypeError("width must be an integer"))
        elif value < 0:
            raise (TypeError("width must be > 0"))
        self.__width = value

    @property
    def height(self):
        """Height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height."""
        if not type(value) is int:
            raise (TypeError("height must be an integer"))
        elif value < 0:
            raise (TypeError("height must be > 0"))
        self.__height = value

    @property
    def x(self):
        """X val."""
        return self.__x

    @x.setter
    def x(self, value):
        """X set."""
        if not type(value) is int:
            raise (TypeError("x must be an integer"))
        elif value < 0:
            raise (TypeError("x must be >= 0"))
        self.__x = value

    @property
    def y(self):
        """Y val."""
        return self.__y

    @y.setter
    def y(self, value):
        """Y set."""
        if not type(value) is int:
            raise (TypeError("y must be an integer"))
        elif value < 0:
            raise (TypeError("y must be >= 0"))
        self.__y = value

    def area(self):
        """Cal area."""
        return self.__height * self.__width

    def display(self):
        """Print Rectangle."""
        if self.__height == 0 or self.__width == 0:
            return
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print("{}{}".format(" " * self.__x, "#" * self.__width))

    def __str__(self):
        """Str callback."""
        return f"[Rectangle] ({self.id}) {self.__x}/"\
            + f"{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Update."""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """To Dict."""
        return {
            'x': self.x,
            'width': self.width,
            'id': self.id,
            'height': self.height,
            'y': self.y
        }

    def to_csv_row(self):
        """To CSV Row."""
        return [self.id, self.width, self.height, self.x, self.y]
