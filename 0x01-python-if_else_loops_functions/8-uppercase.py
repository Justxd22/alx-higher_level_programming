#!/usr/bin/python3
def uppercase(str):
    for i in str:
        case = (ord(i) >= 97 and ord(i) <= 122)
        s = "{}".format(i)
        print(s if not case else chr(ord(i) - 32), end="" if i != str[-1] else "\n")
