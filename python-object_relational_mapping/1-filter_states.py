#!/usr/bin/python3
""""" that lists all states with a name starting with N"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        user = argv[1],
        password = argv[2],
        database = argv[3]
    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id")
    for x in cursor.fetchall():
        if x[1][0] == 'N':
            print(x)
    if cursor:
        cursor.exit()
    if db:
        db.exit()
