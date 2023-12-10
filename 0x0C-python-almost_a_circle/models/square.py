#!/usr/bin/python3
"""Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square.

    Attributes:
        Rectangle Class
    """

    __nb_objects = 0

    def __init__(self, size, x=0, y=0, id=None):
        """Init."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size."""
        return self.width

    @size.setter
    def size(self, value):
        """Size."""
        if not type(value) is int:
            raise (TypeError("width must be an integer"))
        elif value < 0:
            raise (TypeError("width must be > 0"))
        self.width = value
        self.height = value

    def __str__(self):
        """Str callback."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update."""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """To Dict."""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.width,
            'y': self.y
        }

    def to_csv_row(self):
        """To CSV Row."""
        return [self.id, self.size, self.x, self.y]
