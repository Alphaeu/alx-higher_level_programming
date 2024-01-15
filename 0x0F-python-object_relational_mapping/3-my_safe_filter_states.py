#!/usr/bin/python3
"""
Python script that uses MySQLdb to display all values 
matching a given name in the states table of the database hbtn_0e_0_usa
Results are ordered by ascending states.id.
Safe from SQL injections
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
