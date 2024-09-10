WITH Load_Data AS (
    SELECT 
         sku
        ,requested_quantity
        ,cancelled_quantity
        ,requested_quantity - cancelled_quantity AS removal_quantity
    FROM 
        {{ ref('fct_Amz_Removal_Report') }}

),

Group_By_Sku AS (
    SELECT 
        sku
        ,SUM(requested_quantity)    AS total_requested_quantity
        ,SUM(cancelled_quantity)    AS total_cancelled_quantity
        ,SUM(removal_quantity)      AS total_removal_quantity
    FROM 
        Load_Data
    GROUP BY 
        sku
        
)

SELECT 
    *
FROM 
    Group_By_Sku