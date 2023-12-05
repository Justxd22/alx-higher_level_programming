#!/usr/bin/python3
"""FromJsonString."""
import json


def from_json_string(my_str):
    """
    Return list/dict/(Python data structure) from json.

    Parameters:
    - my_str: JSON

    Returns:
    - list/dict/(Python data structure)
    """
    return json.loads(my_str)
