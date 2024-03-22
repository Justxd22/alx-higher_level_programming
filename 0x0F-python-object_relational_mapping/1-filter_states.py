#!/usr/bin/python3
"""Py sql."""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name like binary 'N%'\
                ORDER BY states.id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
