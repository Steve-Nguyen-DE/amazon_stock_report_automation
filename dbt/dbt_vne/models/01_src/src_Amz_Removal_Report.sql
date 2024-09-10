WITH Load_Amz_Order_Items AS (
    SELECT 
	    *
    FROM 
        {{ source('vne', 'Removal') }}

)

SELECT 
    *
FROM 
    Load_Amz_Order_Items