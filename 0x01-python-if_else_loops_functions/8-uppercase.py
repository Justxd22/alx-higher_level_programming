#!/usr/bin/python3
def uppercase(str):
    x = 0
    for i in str:
        case = (ord(i) >= 97 and ord(i) <= 122)
        case2 = (x != len(str) - 1)
        s = "{}".format(i)
        print(chr(ord(i) - 32) if case else s, end="")
        x += 1
    print()
