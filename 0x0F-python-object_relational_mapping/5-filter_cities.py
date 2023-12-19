#!/usr/bin/python3
"""a script to update a db based on some instructions"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", db=sys.argv[3],
                         user=sys.argv[1], passwd=sys.argv[2],
                         port=3306)
    cur = db.cursor()
    cur.execute(""""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
