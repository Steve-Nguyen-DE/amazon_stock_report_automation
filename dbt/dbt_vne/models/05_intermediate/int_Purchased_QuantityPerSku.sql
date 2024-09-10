WITH Load_Data AS (
    SELECT 
    	sku
        ,SUM(final_quantity) AS total_purchased_quantity
    FROM 
        {{ ref('fct_VneAmzPurchasingOrdersDetail') }}
    GROUP BY 
        sku
)

SELECT 
    *
FROM 
    Load_Data