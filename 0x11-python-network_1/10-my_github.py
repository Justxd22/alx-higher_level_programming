#!/usr/bin/python3
"""Requests check status."""
from requests.auth import HTTPBasicAuth
import requests
import sys


if __name__ == "__main__":
    a = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=a)
    print(r.json().get("id"))
