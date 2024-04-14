#!/usr/bin/python3
"""
A script that takes in an argument
and displays all values in the states
table of hbtn_0e_0_usa where name matches
the argument
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
    search_states = """
    SELECT * FROM states WHERE BINARY name = '{}'
    """
    arg = sys.argv[4]
    cur.execute(search_states.format(arg))
    states = cur.fetchall()
    for state in states:
        print(state)
