#!/usr/bin/python3
"""
Script that display all values in the states table of hbtn_0e_0_usa
 where name matches the argument
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    name = argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    crs = db.cursor()
    crs.execute("SELECT * FROM states WHERE name='{}'\
                ORDER BY id ASC".format(name))
    rows = crs.fetchall()
    for rw in rows:
        print(rw)
    crs.close()
    db.close()
