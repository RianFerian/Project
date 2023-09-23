import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')

# Create a cursor
cursor = conn.cursor()

# Query
query = '''SELECT name FROM sqlite_master WHERE type='table';'''

# Execute a query to fetch table names
cursor.execute(query)

# Fetch all table names
table_names = cursor.fetchall()

# Close the cursor and connection
cursor.close()
conn.close()

# Print the table names
for table in table_names:
    print(table[0])