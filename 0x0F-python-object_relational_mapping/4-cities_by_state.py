#!/usr/bin/python3
"""Py sql."""


def main(args):
    """Py sql."""
    if len(args) < 4:
        raise Exception("pass args please")
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities c\
                JOIN states s ON s.id=c.state_id ORDER BY c.id")
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    import sys
    import MySQLdb
    main(sys.argv)
