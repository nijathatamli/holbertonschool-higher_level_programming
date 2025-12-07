#!/usr/bin/python3
""" that takes in the name of a state as an argument and lists all cities of that state, """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT cities.name, states.name \
                    FROM cities \
                    INNER JOIN states on states.id = cities.state_id ")
    for x in cursor.fetchall():
        print(x)
    if cursor:
        cursor.close()
    if db:
        db.close()
