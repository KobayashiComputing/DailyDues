import sqlite3

def getDatabaseCursor(db):
    # Connect to the database (or create it if it doesn't exist)
    connection = sqlite3.connect(db)

    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM sqlite_schema WHERE type = 'table' ORDER BY name;")
    tblList = cursor.fetchall()
    if len(tblList) == 0:
        dbEmpty = True
        print(f"Database {db} is empty... probably newly created...")
    else:
        dbEmpty = False
        print(f"Database {db} has tables:\n{tblList}")

    return connection, cursor, dbEmpty

def saveDatabase(conn):
    # Commit changes and close the connection
    conn.commit()
    conn.close()


def doQuery(cursor):
    # Example: Create a table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
    """)

