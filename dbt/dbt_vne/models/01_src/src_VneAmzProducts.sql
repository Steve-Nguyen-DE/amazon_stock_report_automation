WITH Load_Vne_Products AS (
    SELECT 
	    *
    FROM 
        {{ source('vne', 'VneAmzProducts') }}

)

SELECT 
    *
FROM 
    Load_Vne_Products
