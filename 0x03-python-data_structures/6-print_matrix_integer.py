#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    e = " "
    for i in matrix:
        for x in i:
            print("{:d}".format(x), end=e if i.index(x) != len(i) - 1 else "")
        print("")
