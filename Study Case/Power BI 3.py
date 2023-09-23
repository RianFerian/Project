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
                *
        FROM
                (
                SELECT
                        AllInventories.InventoryId, 
                        AllInventories.Description,
                        Beginning_Summ."Beginning on Hand",
                        Purchase_Summ."Purchase QTY",
                        "Total Sales QTY",
                        Ending_Summ."Ending on Hand",                
                        COALESCE("Beginning on Hand", 0) + COALESCE("Purchase QTY", 0) AS "Total Item"
                FROM
                        (
                        SELECT 
                                InventoryId,
                                Description
                        FROM 
                                "Beginning Inventory"
                        UNION
                        SELECT
                                InventoryId,
                                Description
                        FROM 
                                Purchases
                        UNION
                        SELECT
                                InventoryId,
                                Description
                        FROM 
                                Sales
                        UNION
                        SELECT
                                InventoryId,
                                Description
                        FROM
                                "Ending Inventory"
                        )   AS AllInventories
                LEFT JOIN
                        (
                        SELECT 
                                InventoryId, 
                                onHand AS "Beginning on Hand"
                        FROM 
                                "Beginning Inventory"
                        ) AS Beginning_Summ
                ON
                        AllInventories.InventoryId = Beginning_Summ.InventoryId
                LEFT JOIN
                        (
                        SELECT
                                InventoryId,
                                SUM(Quantity) AS "Purchase QTY"
                        FROM
                                Purchases
                        GROUP BY
                                InventoryId
                        ) AS Purchase_Summ
                ON 
                        AllInventories.InventoryId = Purchase_Summ.InventoryId
                LEFT JOIN
                        (
                        SELECT 
                                InventoryId, 
                                SUM(SalesQuantity) AS "Total Sales QTY"
                        FROM
                                Sales
                        GROUP BY
                                InventoryId
                        ) AS Sales_Summ
                ON 
                        AllInventories.InventoryId = Sales_Summ.InventoryId
                LEFT JOIN
                        (
                        SELECT
                                InventoryId,
                                onHand AS "Ending on Hand"
                        FROM
                                "Ending Inventory"
                        ) AS Ending_Summ
                ON 
                        AllInventories.InventoryId = Ending_Summ.InventoryId
                ) AS difference_subquery
                WHERE "Total Sales QTY" IS NULL AND "Total Item" > 0

'''

## Make a dataframe
df = pd.read_sql_query(query, conn)
df.to_csv("Unsold.csv", index=False)

# Close the cursor and connection
print(df)

conn.close()


#082F53
#C4E2FF