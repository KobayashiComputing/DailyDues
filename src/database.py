import sqlite3

def getDatabaseCursor(db):
    # Connect to the database (or create it if it doesn't exist)
    connection = sqlite3.connect(db)

    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()

    return connection, cursor

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

