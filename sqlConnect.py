import sqlite3

def connect_to_db(db_name):
    try:
        # Connect to the SQLite database (it will create the database file if it doesn't exist)
        connection = sqlite3.connect(db_name)
        print(f"Successfully connected to the database: {db_name}")
        return connection
    except sqlite3.Error as e:
        print(f"Error while connecting to the database: {e}")
        return None
    
def readAllRecords(connection):
    try:
        cursor = connection.cursor()

        read_records_query = '''SELECT * FROM Employee
                            );'''
        cursor.execute(read_records_query)
        connection.commit()
        print("All records retrieved!")

    except sqlite3.Error as e:
        print(f"Error while reading from the table: {e}")

def create_table(connection):
    try:
        # Create a cursor object
        cursor = connection.cursor()

        # SQL query to create a table (example: users table)
        create_table_query = '''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                age INTEGER NOT NULL
                            );'''
        # Execute the SQL query
        cursor.execute(create_table_query)

        # Commit the changes
        connection.commit()
        print("Table created successfully or already exists.")
    except sqlite3.Error as e:
        print(f"Error while creating the table: {e}")

def close_connection(connection):
    try:
        # Close the connection to the database
        if connection:
            connection.close()
            print("Connection closed.")
    except sqlite3.Error as e:
        print(f"Error while closing the connection: {e}")

if __name__ == "__main__":
    db_name = "my_database.db"  # Name of the database file
    connection = connect_to_db(db_name)
    
    if connection:
        create_table(connection)  # Create the table if the connection is successful
        close_connection(connection)  # Close the connection
