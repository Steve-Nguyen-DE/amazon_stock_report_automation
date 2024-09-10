WITH Load_Data AS (
    SELECT 
        *
    FROM 
        {{ ref('stg_VneAmzPurchasingOrdersDetail') }}
    WHERE 
        imported_to_fba_warehouse = TRUE
)

SELECT 
     sku
    ,SUM(final_quantity)            AS total_purchased_quantity
    ,AVG(purchasing_price)          AS average_purchased_price
    ,SUM(final_po_amount)           AS total_purchased_amount
FROM
    Load_Data
GROUP by 
    sku
ORDER BY 
    sku

