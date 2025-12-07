#!/usr/bin/python3
"""""that lists all cities from the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    
    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT c.id, c.cities, s.name \
                    FROM cities AS c \
                    INNER JOIN states AS s ON s.id = c.state_id")
    for x in cursor.fetchall():
        print(x)
    if cursor:
        cursor.close()
    if db:
        db.close()
