#!/usr/bin/python3
"""Py sql."""
import sys
import MySQLdb


def main(args):
    """Py sql."""
    if len(args) < 4:
        raise Exception("pass args please")
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    main(sys.argv)
