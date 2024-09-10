WITH Sales_Data AS (

    SELECT
    seller_sku
    ,SUM(quantity_ordered) FILTER (WHERE purchase_time_stamp_la >= (CURRENT_TIMESTAMP - INTERVAL '3 days') AND purchase_time_stamp_la < (CURRENT_TIMESTAMP - INTERVAL '1 day'))     AS sold_quantity_last_3_days
    ,SUM(quantity_ordered) FILTER (WHERE purchase_time_stamp_la >= (CURRENT_TIMESTAMP - INTERVAL '7 days') AND purchase_time_stamp_la < (CURRENT_TIMESTAMP - INTERVAL '1 day'))     AS sold_quantity_last_7_days
    ,SUM(quantity_ordered) FILTER (WHERE purchase_time_stamp_la >= (CURRENT_TIMESTAMP - INTERVAL '30 days') AND purchase_time_stamp_la < (CURRENT_TIMESTAMP - INTERVAL '1 day'))    AS sold_quantity_last_30_days
    ,SUM(quantity_ordered)                                                                                                                                                          AS total_sold_quantity
    FROM 
        {{ ref('fct_Amz_Order_Items') }}
    GROUP BY seller_sku
)

SELECT 
    *
FROM 
    Sales_Data




