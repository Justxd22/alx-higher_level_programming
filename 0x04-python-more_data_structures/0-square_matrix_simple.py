#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix != [] or matrix is None:
        return [[s * s for s in x] for x in matrix]
