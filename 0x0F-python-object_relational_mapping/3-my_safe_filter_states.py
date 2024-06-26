#!/usr/bin/python3
"""
a script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument but
 safe from MySQL injections!
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
    search_state = """
    SELECT * FROM states WHERE BINARY name = %s
    """
    state_name = sys.argv[4]
    cur.execute(search_state, (state_name,))
    states = cur.fetchall()
    for state in states:
        print(state)
