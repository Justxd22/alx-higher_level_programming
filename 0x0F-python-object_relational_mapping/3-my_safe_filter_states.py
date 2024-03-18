#!/usr/bin/python3
"""Py sql."""


def main(args):
    """Py sql."""
    if len(args) < 5:
        raise Exception("pass args please")
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name like %s\
                ORDER BY id ASC", args[4])
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    import sys
    import MySQLdb
    main(sys.argv)
