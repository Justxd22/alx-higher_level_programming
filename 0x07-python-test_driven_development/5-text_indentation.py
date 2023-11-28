#!/usr/bin/python3
"""Text indentation."""


def text_indentation(text):
    """Text indention."""
    beg = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for idx, val in enumerate(text):
        if val in '?:.':
            print(text[beg:idx + 1].strip() + '\n')
            beg = idx + 1
    if not beg:
        print(text, end='')
    elif beg is not len(text):
        print(text[beg:idx + 1].strip(), end='')
