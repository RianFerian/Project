import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')

# Create a cursor
cursor = conn.cursor()

## KEY VALUE
## InventoryId

# Query SQL
query = '''
        SELECT
            InventoryId,
            VendorName,
            SUM(Quantity),
            PODate
        FROM
            Purchases
        GROUP BY
            InventoryId
                
'''

## Make a dataframe
df = pd.read_sql_query(query, conn)
df.to_csv("Purchaser Data.csv", index=False)

# Close the cursor and connection
print(df)

conn.close()