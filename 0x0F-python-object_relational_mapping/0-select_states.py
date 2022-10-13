#!/usr/bin/python3
"""Creating a script that list all the states
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    db_rows = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    base_connector = db_rows.cursor()
    base_connector.execute("SELECT * FROM states ORDER BY states.id ASC;")
    db_rows = base_connector.fetchall()
    for info_row in db_rows:
        print(info_row)
