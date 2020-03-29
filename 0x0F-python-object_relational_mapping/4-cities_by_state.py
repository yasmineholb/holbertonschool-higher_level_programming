#!/usr/bin/python3
""" db connection """
import MySQLdb
from sys import argv
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         db=argv[3]
                         )
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name "
                "FROM cities AS c JOIN states AS s ON c.state_id = s.id "
                "ORDER BY c.id ASC")
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    db.close()
