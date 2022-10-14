#!/usr/bin/python3
'''script that list states that start with "N" in the database'''


if __name__ == '__main__':
    import sys
    import MySQLdb

    base_database = MySQLdb.connect(host='localhost', port=3306,
                                    user=sys.argv[1], passwd=sys.argv[2],
                                    db=sys.argv[3])

    my_database = base_database.cursor()
    my_database.execute("""SELECT * FROM states WHERE
                        CAST(name AS BINARY) LIKE 'N%';""")
    base_database = my_database.fetchall()
    for info_row in base_database:
        print("{}".format(info_row))
