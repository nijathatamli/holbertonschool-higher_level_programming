#!/usr/bin/python3
"""""that takes in an argument and displays all values"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT *  \
    FROM `states` \
     WHERE BINARY `name` = '{}' \
     ORDER BY id".format(argv[4]))
    for x in cursor.fetchall():
        print(x)
    if cursor:
        cursor.close()
    if db:
        db.close()
