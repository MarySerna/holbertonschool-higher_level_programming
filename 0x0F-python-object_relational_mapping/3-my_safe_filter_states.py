#!/usr/bin/python3
"""
Script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa where name matches the argument
But this time, write one that is safe from MySQL injections!
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    st_name = argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    crs = db.cursor()
    crs.execute("SELECT * FROM states WHERE name=%s \
                ORDER BY states.id ASC", (st_name,))
    rows = crs.fetchall()
    for rw in rows:
        print(rw)
    crs.close()
    db.close()
