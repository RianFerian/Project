import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')

# Query SQL
query = '''
        SELECT *
        FROM "Sales"
        LIMIT 5

'''

# Make a dataframe
df = pd.read_sql_query(query, conn)


# Close the cursor and connection
print(query)
print(df)

conn.close()

