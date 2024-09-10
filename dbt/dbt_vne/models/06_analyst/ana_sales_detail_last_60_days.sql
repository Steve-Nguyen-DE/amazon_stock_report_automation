SELECT 
    *
FROM 
    {{ ref('fct_Amz_Order_Items') }}
WHERE 
    purchase_time_stamp >= NOW() - INTERVAL '60 days'
ORDER BY 
    purchase_time_stamp DESC