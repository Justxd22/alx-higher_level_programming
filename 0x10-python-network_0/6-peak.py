#!/usr/bin/python3
"""Find peak."""


def search(lo, h, ints):
    """Find peak."""
    mid = (lo + h) // 2
    if lo == h:
        return ints[h]
    if ints[mid] < ints[mid + 1]:
        return (search(mid + 1, h, ints))
    return (search(lo, mid, ints))


def find_peak(ints):
    """Find peak."""
    if not ints:
        return
    return (search(0, len(ints) - 1, ints))
