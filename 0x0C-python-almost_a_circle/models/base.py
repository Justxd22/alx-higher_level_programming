#!/usr/bin/python3
"""Base."""
import json
import csv
import turtle


class Base():
    """
    Base.

    Attributes:
        pass
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Init."""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """To Json String."""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save To File."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_string = cls.to_json_string([obj.to_dictionary()
                                              for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Load From Json."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, *args, **kwargs):
        """Create."""
        dummy_instance = cls(1, 1)
        args = [int(arg) for arg in args]
        dummy_instance.update(*args, **kwargs)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Load From File."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                dictionaries = cls.from_json_string(json_data)
                instances = [cls.create(**data) for data in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save to CSV."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """Load to CSV."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                instances = [cls.create(*row) for row in reader]
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rect/Square."""
        screen = turtle.Screen()
        screen.bgcolor("white")

        for rect in list_rectangles:
            draw_rectangle(rect)

        for square in list_squares:
            draw_square(square)

        turtle.done()


def draw_rectangle(rectangle):
    """Draw Rectangle."""
    turtle.penup()
    turtle.goto(rectangle.x, rectangle.y)
    turtle.pendown()
    turtle.forward(rectangle.width)
    turtle.left(90)
    turtle.forward(rectangle.height)
    turtle.left(90)
    turtle.forward(rectangle.width)
    turtle.left(90)
    turtle.forward(rectangle.height)
    turtle.left(90)


def draw_square(square):
    """Draw Square."""
    turtle.penup()
    turtle.goto(square.x, square.y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(square.size)
        turtle.left(90)
