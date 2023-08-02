#!/usr/bin/python3
"""Takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    """State name searched"""
    state_name = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}' \
                ORDER BY states.id".format(state_name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()