#!/usr/bin/python3
"""script that takes info from user and displays the result from the database
"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    base_connector = MySQLdb.connect(host='localhost', port=3306,
                                     user=sys.argv[1], passwd=sys.argv[2],
                                     db=sys.argv[3])
    states_query = sys.argv[4]
    db_connected = base_connector.cursor()
    db_connected.execute("""SELECT * FROM states WHERE\
                         CAST(name AS BINARY) LIKE '{}'\
                         ORDER BY states.id ASC;"""
                         .format(states_query))
    base_connector = db_connected.fetchall()
    for info in base_connector:
        print(info)
