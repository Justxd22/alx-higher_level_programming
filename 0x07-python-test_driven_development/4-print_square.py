#!/usr/bin/python3
"""Print square."""


def print_square(size):
    """Print square.

    Parameters:
    - matrix: must be a list of lists of integers or floats
    - div: must be a number (integer or float)
    """
    if size == 0:
        return
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    print('\n'.join('#' * size for x in range(size)))
