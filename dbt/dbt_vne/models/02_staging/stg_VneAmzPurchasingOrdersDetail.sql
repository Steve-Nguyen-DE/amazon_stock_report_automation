WITH Raw_PO_Details AS (
    SELECT 
         order_date
        ,po_id
        ,amazon_shipment_id
        ,sku
        ,CAST(NULLIF(final_quantity, '') AS BIGINT) AS 	final_quantity
        ,purchasing_price
        ,po_amount
        ,final_po_amount
        ,payment_status
        ,CAST(imported_to_fba_warehouse AS BOOLEAN) AS  imported_to_fba_warehouse
    FROM
        {{ ref('rename_VneAmzPurchasingOrdersDetail') }}
)

SELECT 
    *
FROM 
    Raw_PO_Details
