WITH Order_Items AS (
    SELECT 
        *
    FROM 
        {{ ref('src_Amz_Order_items') }}
),

Orders AS(
    SELECT 
         amazon_order_id
        ,purchase_time_stamp
        ,purchase_time_stamp_la
        ,last_update_time_stamp
        ,last_update_time_stamp_la
    FROM 
        {{ ref('rename_Amz_Orders') }}
),

Join_Data AS (
    SELECT 
         Orders.purchase_time_stamp
        ,Orders.purchase_time_stamp_la
        ,Orders.last_update_time_stamp
        ,Orders.last_update_time_stamp_la
        ,Order_Items.*
    FROM 
        Orders
        RIGHT JOIN 
        Order_Items
            ON Orders.amazon_order_id = Order_Items.order_id
)

SELECT 
    *
FROM 
    Join_Data