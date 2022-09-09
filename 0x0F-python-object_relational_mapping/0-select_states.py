#!/usr/bin/python3
"""Python script to list all states in database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql username> <mysql password> <db name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]