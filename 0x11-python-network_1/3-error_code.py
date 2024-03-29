#!/usr/bin/python3
"""Urllib check status."""
import urllib.request
import urllib.parse
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as re:
            print(re.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
