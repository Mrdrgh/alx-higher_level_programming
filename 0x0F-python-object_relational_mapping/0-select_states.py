#!/usr/bin/python3
"""lists all the states from the db in the arguments"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", db=sys.argv[3], user=sys.argv[0],
                         passwd=sys.argv[2], port=3306)
    cursr = db.cursor()
    cursr.execute("SELECT * FROM states")
    res = cursr.fetchall()
    for ress in res:
        print(ress)
    cursr.close()
    db.close()
    



