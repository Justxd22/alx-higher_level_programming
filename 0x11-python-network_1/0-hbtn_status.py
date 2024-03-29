#!/usr/bin/python3
"""Urllib check status."""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        res = res.read()

    print('Body response:\n\t- type: {}'.format(type(res)))
    print('\t- content: {}'.format(res))
    print('\t- utf8 content: {}'.format(res.decode('utf-8')))
