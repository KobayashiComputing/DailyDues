import sqlite3
import datetime

def dbGetDatabaseCursor(db):
    # Connect to the database (or create it if it doesn't exist)
    connection = sqlite3.connect(db)

    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM sqlite_schema WHERE type = 'table' ORDER BY name;")
    tblList = cursor.fetchall()
    if len(tblList) == 0:
        dbEmpty = True
        # print(f"Database {db} is empty... probably newly created...")
    else:
        dbEmpty = False
        # print(f"Database {db} has tables:\n{tblList}")

    return connection, cursor, dbEmpty

def dbInitDatabase(cursor):
    dbVersion = "0.00a"
    dbDTG = datetime.datetime.now()
    dbDTGstr = dbDTG.strftime("%I:%M%p on %B %d, %Y")
    dbDTGstr = dbDTG.isoformat()
    
    # create and populate the 'dd_info' table...
    sqlQuery = ""
    sqlQuery += "CREATE TABLE IF NOT EXISTS dd_info"
    sqlQuery += " (version TEXT NOT NULL,"
    sqlQuery += "  create_on_raw TEXT NOT NULL,"
    sqlQuery += "  created_on_txt TEXT NOT NULL);"
    cursor.execute(sqlQuery)
    sqlQuery = f'insert into dd_info values("{dbVersion}", "{dbDTG}", "{dbDTGstr}");'
    cursor.execute(sqlQuery)

    # create the 'tasks' table...
    sqlQuery = ""
    sqlQuery += "CREATE TABLE IF NOT EXISTS tasks ("
    sqlQuery += "  name TEXT NOT NULL,"
    sqlQuery += "  description TEXT NOT NULL,"
    sqlQuery += "  priority TEXT NOT NULL,"
    sqlQuery += "  frequency TEXT NOT NULL,"
    sqlQuery += "  reset TEXT NOT NULL,"
    sqlQuery += "  target TEXT NOT NULL,"
    sqlQuery += "  created TEXT NOT NULL,"
    sqlQuery += "  state TEXT NOT NULL,"
    sqlQuery += "  time_total TEXT,"
    sqlQuery += "  time_session TEXT,"
    sqlQuery += "  dtg_session_paused TEXT,"
    sqlQuery += "  dtg_session_start TEXT,"
    sqlQuery += "  dtg_session_stop TEXT"
    sqlQuery += ");"
    cursor.execute(sqlQuery)

    # all done, so return...
    return dbVersion

def dbGetTaskData(cursor):
    # Get column names
    cursor.execute("PRAGMA table_info(tasks);")
    info = cursor.fetchall()
    # columns = [column[1] for column in cursor.fetchall()]    
    columns = [column[1] for column in info]    

    # Get the row data    
    rows = []
    sqlQuery = "SELECT * FROM tasks;"
    cursor.execute(sqlQuery)
    rows = cursor.fetchall()

    return info, columns, rows

def dbUpdate(cursor, table, key=(None, None), values={}):
    # determine if the record with the given key already exists
    sqlQuery = f"SELECT EXISTS(SELECT 1 FROM {table} WHERE {key[0]} = '{key[1]}');"
    cursor.execute(sqlQuery)
    rowExists = cursor.fetchone()[0]
    
    if rowExists:
        # record exists, so this is an update...
        # print(f"Table '{table}' contains a record with '{key[0]}' == '{key[1]}'")
        # basic update statement for sqlite3:
        #   UPDATE employees
        #       SET name = 'John Doe',
        #           age = 30
        #       WHERE id = 1;
        sqlQuery = f"update {table} set "
        needsComma = False
        for field, data in values.items():
            if needsComma:
                sqlQuery += ", "
            needsComma = True
            sqlQuery += f"{field} = '{data}'"

        sqlQuery += f" where {key[0]} = '{key[1]}';"

    else:
        # record does not exist, so this is an insert...
        # print(f"Record with field '{key[0]}' == '{key[1]}' was not found in table '{table}'")
        fieldList = ""
        dataList = ""
        needsComma = False
        for field, data in values.items():
            if needsComma:
                fieldList += ", "
                dataList += ", "
            needsComma = True
            fieldList += f"{field}"
            dataList += f"'{data}'"

        sqlQuery = f"insert into {table} ({fieldList}) values ({dataList});"

    cursor.execute(sqlQuery)
    pass


def dbCommit(connection):
    connection.commit()

def dbSaveDatabase(conn):
    # Commit changes and close the connection
    conn.commit()
    conn.close()


def dbDoQuery(cursor):
    # Example: Create a table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
    """)

