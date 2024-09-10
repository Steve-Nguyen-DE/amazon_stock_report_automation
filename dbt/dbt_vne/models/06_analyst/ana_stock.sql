WITH Sales AS(
    SELECT 
        *
    FROM 
        {{ ref('int_TimePeriods_SalesPer_Sku') }}
),

Purchase AS(
    SELECT
        sku
        ,total_purchased_quantity
    FROM 
        {{ ref('int_VneAmzPurchasingOrders') }}
),

Removal AS (
    SELECT 
        sku 
        ,total_removal_quantity
    FROM 
        {{ ref('int_Removal_QuantityPerSku') }}
),

db AS (
    SELECT 
        parent_sku
        ,sku
        ,product_type
        ,box_type
        ,color
        ,fan_quantity
        ,d
        ,product_length
        ,curl
        ,box_dimension
        ,product_name
    FROM 
        {{ ref('rename_VneAmzProducts') }}
),

Join_Data AS (
    SELECT 
        db.parent_sku
        ,Purchase.sku                           AS purchase_sku
        ,sales.*
        ,Purchase.total_purchased_quantity
        ,Removal.total_removal_quantity
        ,db.product_type
        ,db.box_type
        ,db.color
        ,db.fan_quantity
        ,db.d
        ,db.product_length
        ,db.curl
        ,db.box_dimension
        ,db.product_name
    FROM 
        Sales
        RIGHT JOIN 
        Purchase
            ON sales.seller_sku = Purchase.sku
        LEFT JOIN
        Removal
            ON Purchase.sku = Removal.sku
        LEFT JOIN 
        db
            ON Purchase.sku = db.sku


),

Add_Stock AS (
    SELECT
         *
        ,total_purchased_quantity - COALESCE(total_sold_quantity,0) - COALESCE(total_removal_quantity,0) AS current_stock_quantity
    FROM 
        Join_Data

),

Add_Stock_Level_days AS (
    SELECT 
        *
        ,current_stock_quantity / NULLIF(sold_quantity_last_30_days / (30::FLOAT), 0) AS stock_level
    FROM
        Add_Stock
)

SELECT 
    *
FROM 
    Add_Stock_Level_days
ORDER BY 
    parent_sku

