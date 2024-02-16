#!/usr/bin/python3
""" A safe from MySQL injections script that takes in an argument
    and displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    connection = MySQLdb.connect(host='localhost',
                                 user=argv[1],
                                 passwd=argv[2],
                                 db=argv[3],
                                 port=3306)

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states WHERE name = %s\
                    ORDER BY id ASC", (argv[4],))

    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()
