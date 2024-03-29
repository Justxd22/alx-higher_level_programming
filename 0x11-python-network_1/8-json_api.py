#!/usr/bin/python3
"""Requests check status."""
import requests
import sys

if __name__ == "__main__":
    q = ""
    if len(sys.argv) == 2:
        q = sys.argv[1]
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        d = req.json()
        idd = d.get('id')
        name = d.get('name')
        if len(d) == 0 or not idd or not name:
            print("No result")
        else:
            print("[{}] {}".format(idd, name))
    except Exception as e:
        print("Not a valid JSON")
