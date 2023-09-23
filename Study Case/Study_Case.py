# Import library
import pandas as pd
import sqlite3

# Read Files
Beginning_Inventory = pd.read_csv('Study Case\\Beginning Inventory.csv' , encoding='latin-1')
Ending_Inventory = pd.read_csv('Study Case\\Ending Inventory.csv' , encoding='latin-1')
Purchases = pd.read_csv('Study Case\\Purchases.csv', encoding='latin-1')
Sales = pd.read_csv('Study Case\\Sales.csv', encoding='latin-1')

# Connect to the database
conn = sqlite3.connect('my_database.db')

# Add files to database
Beginning_Inventory.to_sql('Beginning Inventory', conn, if_exists='replace', index=False)
Ending_Inventory.to_sql('Ending Inventory', conn, if_exists='replace', index=False)
Purchases.to_sql('Purchases', conn, if_exists='replace', index=False)
Sales.to_sql('Sales', conn, if_exists='replace', index=False)

# Commit the changes
conn.commit()
conn.close()