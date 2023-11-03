#!/usr/bin/python3
import sys


def hand_args():
    x = len(sys.argv) - 1

    if x == 0:
        print("0 arguments.")
    else:
        print("{} {}:".format(x, 'argument' if x == 1 else 'arguments'))
        for i in range(1, x + 1):
            print(f"{i}: {sys.argv[i]}")


if __name__ == "__main__":
    hand_args()
