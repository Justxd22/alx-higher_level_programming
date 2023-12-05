#!/usr/bin/python3
"""WriteFile."""


def write_file(filename="", text=""):
    """
    Write string to text file.

    Parameters:
    - filename: file to write
    - text: text to write to file
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
