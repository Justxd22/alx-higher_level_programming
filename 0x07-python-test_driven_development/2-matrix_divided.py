#!/usr/bin/python3
"""Divide matrix Function."""


def matrix_divided(matrix, div):
    """
    Divide matrix Function.

    Parameters:
    - matrix: must be a list of lists of integers or floats
    - div: must be a number (integer or float)
    """
    if (not isinstance(matrix, list)
        or 0 in [len(x) if type(x) is list else 0 for x in matrix]
            or any(False in x for x in
                   [[isinstance(y, (int, float)) for y in r]
                    for r in matrix])):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    elif (len(set([len(x) for x in matrix])) > 1):
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (float, int)):
        return TypeError("div must be a number")
    elif div == 0:
        return ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
