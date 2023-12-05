#!/usr/bin/python3
"""ReadFile."""


def read_file(filename=""):
    """
    Read text file.

    Parameters:
    - filename: file to lookup
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
