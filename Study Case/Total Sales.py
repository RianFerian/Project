import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')

# Query SQL
query = '''
        SELECT InventoryId, Brand, SUM(SalesQuantity) AS "Total Sales QTY"
        FROM "Sales"
        GROUP BY InventoryId, Brand
'''

# Make a dataframe
df = pd.read_sql_query(query, conn)


# Close the cursor and connection
print(query)
print(df)

conn.close()

