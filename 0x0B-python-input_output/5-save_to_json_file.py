#!/usr/bin/python3
"""SaveToJsonFile."""
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
