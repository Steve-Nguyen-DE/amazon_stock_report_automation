WITH Load_Purchasing_Order_Details AS (
    SELECT 
	    *
    FROM 
        {{ source('vne', 'VneAmzPurchasingOrdersDetail') }}

)

SELECT 
    *
FROM 
    Load_Purchasing_Order_Details
