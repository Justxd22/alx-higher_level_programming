#!/usr/bin/python3
def uppercase(str):
    for i in str:
        case = (ord(i) >= 97 and ord(i) <= 122)
        print(i, end="") if not case else print(chr(ord(i) - 32), end="")
    print()
