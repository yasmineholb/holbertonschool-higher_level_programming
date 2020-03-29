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
    cur.execute("SELECT c.name FROM cities AS c INNER JOIN states AS s ON "
                "c.state_id = s.id WHERE s.name = %s "
                "ORDER BY c.id ASC", (argv[4],))
    query = cur.fetchall()
    print(", ".join([row[0] for row in query]))
    cur.close()
    db.close()
