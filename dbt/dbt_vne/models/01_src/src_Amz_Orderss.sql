WITH Load_Amz_Orders AS (
    SELECT 
	    *
    FROM 
        {{ source('vne', 'Orders') }}
)

SELECT 
    *
FROM 
    Load_Amz_Orders
ORDER BY 
    "LastUpdateDate" DESC
