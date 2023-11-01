#!/usr/bin/python3

for i in range(ord('z'), ord('A') - 1, -1):
    s = "{}".format(chr(i - 32))
    if i % 2 == 0:
        s = "{}".format(chr(i))
    print(s, end='')
    if chr(i) == 'A' or chr(i) == 'a':
        break
