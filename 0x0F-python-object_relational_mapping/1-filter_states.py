#!/usr/bin/python3
""" lists all states with a name starting with N from hbtn_0e_0_usa """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    connection = MySQLdb.connect(host='localhost',
                                 user=argv[1],
                                 passwd=argv[2],
                                 db=argv[3],
                                 port=3306)

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                    ORDER BY id ASC")

    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()
