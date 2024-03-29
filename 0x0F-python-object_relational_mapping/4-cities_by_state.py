#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    connection = MySQLdb.connect(host='localhost',
                                 user=argv[1],
                                 passwd=argv[2],
                                 db=argv[3],
                                 port=3306)

    cursor = connection.cursor()

    cursor.execute('SELECT cities.id, cities.name, states.name\
                    FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    ORDER BY cities.id')

    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()
