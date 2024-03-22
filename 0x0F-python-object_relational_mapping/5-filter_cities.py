#!/usr/bin/python3
"""Py sql."""


def main(args):
    """Py sql."""
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM\
                cities INNER JOIN states ON states.id=cities.state_id\
                WHERE states.name=%s", (sys.argv[4],))
    states = cur.fetchall()
    print(", ".join(map(lambda x: "%s" % x, states)))
    cur.close()
    db.close()


if __name__ == "__main__":
    import sys
    import MySQLdb
    main(sys.argv)
