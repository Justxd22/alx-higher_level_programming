#!/usr/bin/python3
"""AddItem."""

from sys import argv
from os.path import exists
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object as json to a text file.

    Parameters:
    - my_obj: object
    - filename: file name
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """
    Create an object from JSON file.

    Parameters:
    - filename: file name

    Returns:
    - Python object
    """
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


file = "add_item.json"

if exists(file):
    list = load_from_json_file(file)
else:
    list = []

list.extend(argv[1:])

save_to_json_file(list, file)
