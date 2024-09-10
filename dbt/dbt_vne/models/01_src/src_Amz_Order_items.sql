WITH Load_Amz_Order_Items AS (
    SELECT 
	    *
    FROM 
        {{ source('vne', 'OrderItems') }}
)

SELECT 
    *
FROM 
    Load_Amz_Order_Items
    
