#!/usr/bin/python3
""" Script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
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

    query = "SELECT * FROM states WHERE BINARY name = '{}'\
             ORDER BY id ASC".format(argv[4])
    cursor.execute(query)

    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()
