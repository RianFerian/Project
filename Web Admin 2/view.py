import sqlite3
import os


# Get the directory containing the currently executing Python script
folder_path = os.path.dirname(os.path.abspath(__file__))

# Connect to the database file inside the specified folder
db_path = os.path.join(folder_path, 'mydatabase.db')

# Connect to the SQLite database
connection = sqlite3.connect(db_path)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Execute a SELECT query to fetch all rows from the 'employee' table
cursor.execute("SELECT * FROM employee")

# Fetch all rows from the result set
data = cursor.fetchall()

# Print the data
for row in data:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
