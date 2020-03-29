#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    st_name = argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    crs = db.cursor()
    crs.execute("SELECT cities.name FROM cities INNER JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name =%s\
                ORDER BY cities.id ASC", (st_name,))
    rows = crs.fetchall()
    res = []
    for rw in rows:
        res.append(rw[0])
    print(", ".join(res))
    crs.close()
    db.close()
