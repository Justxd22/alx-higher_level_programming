#!/usr/bin/python3
"""LoadFromJsonFile."""
import json


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
