#!/usr/bin/python3
"""Student."""


class Student():
    """Student."""

    def __init__(self, first_name, last_name, age):
        """Init."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Tojson."""
        if (all(isinstance(x, str) for x in attrs)
                and isinstance(attrs, list)):
            return {x: y for x, y in self.__dict__.items() if x in attrs}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes."""
        if(json):
            self.__dict__ = json
