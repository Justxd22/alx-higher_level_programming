#!/usr/bin/python3
"""ToJsonString."""
import json


def to_json_string(my_obj):
    """
    Return JSON.

    Parameters:
    - my_obj: object

    Returns:
    - JSON
    """
    return json.dumps(my_obj)
