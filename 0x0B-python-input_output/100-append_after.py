#!/usr/bin/python3
"""AppendAfter."""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line after each line containing a specific string.

    Parameters:
    - filename: name
    - search_string: string to search
    - new_string: new line
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
