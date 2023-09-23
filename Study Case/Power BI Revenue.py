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
                Sales.InventoryId AS ID,
                Sales.Store,
                Sales.Description,
                SUM(Sales.SalesQuantity),
                SalesPrice AS "Sales Price",
                Sales.ExciseTax AS "Sales Tax",
                Purchase_summ.PurchasePrice,
                Beginning_summ.Price AS "Beginning Price",
                Ending_summ.Price AS "Ending Price",
                CASE
                        WHEN COALESCE(Purchase_summ.PurchasePrice, 0) = 0 THEN
                                CASE
                                        WHEN COALESCE(Beginning_summ.Price, 0) = 0 THEN Ending_summ.Price
                                        ELSE COALESCE(Beginning_summ.Price, 0)
                                END
                        ELSE COALESCE(Purchase_summ.PurchasePrice, 0)
                END AS "Final Price",
                Sales.SalesDate,
                Sales.VendorName
        FROM
                Sales
        LEFT JOIN
                (
                SELECT
                        InventoryId,
                        PurchasePrice
                FROM
                        Purchases
                GROUP BY
                        InventoryId
                ) AS Purchase_summ
        ON
                Sales.InventoryId = Purchase_summ.InventoryId
        LEFT JOIN
                (
                SELECT
                        InventoryId,
                        Price
                FROM
                        "Ending Inventory"
                GROUP BY
                        InventoryId
                ) AS Ending_summ
        ON 
                Sales.InventoryId = Ending_summ.InventoryId
        LEFT JOIN
                (
                SELECT
                        InventoryId,
                        Price
                FROM
                        "Beginning Inventory"
                GROUP BY
                        InventoryId
                ) AS Beginning_summ
        ON 
                Sales.InventoryId = Beginning_summ.InventoryId
        GROUP BY
                ID  
                
'''

## Make a dataframe
df = pd.read_sql_query(query, conn)
df.to_csv("Revenue Data 2.csv", index=False)

# Close the cursor and connection
print(df)

conn.close()