WITH Rename_data AS (
    SELECT
         CAST("request-date" AS TIMESTAMP)                      AS request_date
        ,"order-id"                                             AS order_id
        ,"order-source"                                         AS order_source
        ,"order-type"                                           AS order_type
        ,"order-status"                                         AS order_status
        ,CAST("last-updated-date" AS TIMESTAMP)                 AS last_update_date
        ,                                                          sku
        ,                                                          fnsku
        ,                                                          disposition
        ,CASE 
            WHEN "requested-quantity" IS NULL OR "requested-quantity" = '' THEN 0
            ELSE CAST("requested-quantity" AS INT)
         END AS requested_quantity

        ,CASE 
            WHEN "cancelled-quantity" IS NULL OR "cancelled-quantity" = '' THEN 0
            ELSE CAST("cancelled-quantity" AS INT)
         END AS cancelled_quantity

        ,CASE 
            WHEN "disposed-quantity" IS NULL OR "disposed-quantity" = '' THEN 0
            ELSE CAST("disposed-quantity" AS INT)
         END AS disposed_quantity

        ,CASE 
            WHEN "shipped-quantity" IS NULL OR "shipped-quantity" = '' THEN 0
            ELSE CAST("shipped-quantity" AS INT)
         END AS shipped_quantity

        ,CASE 
            WHEN "in-process-quantity" IS NULL OR "in-process-quantity" = '' THEN 0
            ELSE CAST("in-process-quantity" AS INT)
         END AS in_process_quantity

        ,CASE 
            WHEN "removal-fee" IS NULL OR "removal-fee" = '' THEN 0
            ELSE CAST("removal-fee" AS FLOAT)
         END AS removal_fee

        ,                                                          currency
    FROM 
        {{ ref('src_Amz_Removal_Report') }}
)

SELECT 
    *
FROM 
    Rename_data