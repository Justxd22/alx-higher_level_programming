#!/usr/bin/python3
from sys import argv


def add_args():
    x = len(argv) - 1
    sum = 0

    if x == 0:
        print(0)
        exit()
    else:
        for i in range(1, x + 1):
            sum += int(argv[i])
    print(sum)


if __name__ == "__main__":
    add_args()
