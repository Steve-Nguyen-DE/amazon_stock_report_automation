WITH Load_Data AS (
    SELECT 
        *
    FROM 
        {{ ref('rename_Amz_Removal_Report') }}
)

SELECT 
    * 
FROM 
    Load_Data