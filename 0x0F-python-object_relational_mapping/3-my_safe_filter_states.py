#!/usr/bin/python3
"""Py sql."""
import MySQLdb
import sys


def main(args):
    """Py sql."""
    if len(args) < 5:
        raise Exception("pass args please")
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s\
                ORDER BY id ASC", (args[4], ))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    main(sys.argv)
