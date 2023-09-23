'''
    SELECT
            *,
            CASE
                    WHEN difference = 0 THEN "inventory is Complete"
                    ELSE "inventory is Uncomplete"
            END AS "inventory status"
    FROM
            (
            SELECT
                    AllInventories.InventoryId, 
                    Beginning_Summ."Beginning on Hand",
                    Purchase_Summ."Purchase QTY",
                    "Total Sales QTY",
                    Ending_Summ."Ending on Hand",                
                    COALESCE("Beginning on Hand", 0) + COALESCE("Purchase QTY", 0) - COALESCE("Total Sales QTY", 0) - COALESCE("Ending on Hand", 0) AS difference
            FROM
                    (
                    SELECT 
                            InventoryId
                    FROM 
                            "Beginning Inventory"
                    UNION
                    SELECT
                            InventoryId
                    FROM 
                            Purchases
                    UNION
                    SELECT
                            InventoryId
                    FROM 
                            Sales
                    UNION
                    SELECT
                            InventoryId
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
    WHERE difference <> 0   
'''