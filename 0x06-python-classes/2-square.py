#!/usr/bin/python3
class Square:

    def __init__(self, size=0):
        if not type(size) is int:
            raise (TypeError("size must be an integer"))
        elif size < 0:
            raise (TypeError("size must be >= 0"))
        self.__size = size