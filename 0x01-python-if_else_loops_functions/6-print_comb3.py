#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        c = (i == 8 and x == 9)
        s = "{}".format(i, x)
        print(f"{i}{x}") if c else (print(f"{i}{x}, ", end="") if x > i else 0)
