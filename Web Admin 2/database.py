import sqlite3
import os

# Get the directory containing the currently executing Python script
folder_path = os.path.dirname(os.path.abspath(__file__))

# Connect to the database file inside the specified folder
db_path = os.path.join(folder_path, 'mydatabase.db')

print(db_path)
connection = sqlite3.connect(db_path)

cursor = connection.cursor()

# Example: Creating a 'users' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL
    )
''')

# Commit the changes
connection.commit()

connection.close()
