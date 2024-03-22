#!/usr/bin/python3
"""Py sql."""


def main(args):
    """Py sql."""
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities c\
                JOIN states s ON s.id=c.state_id where s.name=%s\
                ORDER BY c.id", (sys.argv[4],))
    states = cur.fetchall()
    print(", ".join(map(lambda x: "%s" % x, states)))
    cur.close()
    db.close()


if __name__ == "__main__":
    import sys
    import MySQLdb
    main(sys.argv)
