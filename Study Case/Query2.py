import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')

# Create a cursor
cursor = conn.cursor()

# QUERY
query = '''PRAGMA table_info('Sales');'''

# Execute a query to fetch the column names of the 'Beginning Inventory' table
cursor.execute(query)

# Fetch all column names
column_info = cursor.fetchall()

# Extract the column names from the result
column_names = [info[1] for info in column_info]

# Close the cursor and connection
cursor.close()
conn.close()

# Print the column names
print(query)
print(column_names)