#!/usr/bin/python3
"""
A script that lists all cities
from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost")
    cur = db.cursor()
    name_cities = """
    SELECT cities.id, cities.name, states.name
    FROM cities JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cur.execute(name_cities)
    cities = cur.fetchall()
    for city in cities:
        print(city)
