#!/usr/bin/python3
"""AppendWrite."""


def append_write(filename="", text=""):
    """
    Append string at the end of file.

    Parameters:
    - filename: file
    - text: text to append to file
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
