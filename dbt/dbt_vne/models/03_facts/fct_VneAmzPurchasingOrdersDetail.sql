WITH Load_Data AS (
    SELECT 
        *
    FROM 
        {{ ref('stg_VneAmzPurchasingOrdersDetail') }}
)

SELECT  
    *
FROM 
    Load_Data

