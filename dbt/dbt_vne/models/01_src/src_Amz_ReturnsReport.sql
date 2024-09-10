WITH Load_Amz_Order_Items AS (
    SELECT 
        *
    FROM 
        {{ source('vne', 'Returns') }}  
)

SELECT 
    *
FROM 
    Load_Amz_Order_Items
