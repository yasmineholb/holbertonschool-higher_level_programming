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
    cur.execute("SELECT * FROM states WHERE BINARY name='{}' ORDER BY id ASC"
                .format(argv[4]))
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    db.close()
