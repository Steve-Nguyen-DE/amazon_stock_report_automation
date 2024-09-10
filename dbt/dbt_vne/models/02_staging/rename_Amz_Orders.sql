WITH Load_Data AS (
    SELECT 
         "AmazonOrderId"                                                                AS amazon_order_id
        ,"BuyerInfo_BuyerEmail"                                                         AS buyer_email 
        ,CAST("EarliestShipDate" AS TIMESTAMP)                                          AS earliest_ship_time_stamp
        ,"SalesChannel"                                                                 AS sales_chanel
        ,"OrderStatus"                                                                  AS order_status
        ,"NumberOfItemsShipped"                                                         AS number_of_items_shipped
        ,"OrderType"                                                                    AS order_type
        ,"IsPremiumOrder"                                                               AS is_premium_order
        ,"IsPrime"                                                                      AS is_prime 
        ,"FulfillmentChannel"                                                           AS fulfillment_chanel
        ,"NumberOfItemsUnshipped"                                                       AS number_of_items_unshipped 
        ,"HasRegulatedItems"                                                            AS has_regulated_items 
        ,"IsReplacementOrder"                                                           AS is_replacemetn_order 
        ,"IsSoldByAB"                                                                   AS is_sold_by 
        ,CAST("LatestShipDate" AS TIMESTAMP)                                            AS latest_ship_date 
        ,"ShipServiceLevel"                                                             AS shipping_service_level
        ,"IsISPU"                                                                       AS is_ISPU 
        ,"MarketplaceId"                                                                AS marketplace_id 
        ,CAST("PurchaseDate" AS TIMESTAMP)                                              AS purchase_time_stamp
        ,CAST("PurchaseDate" AS TIMESTAMP) AT TIME ZONE 'America/Los_Angeles'           AS purchase_time_stamp_la
        ,"ShippingAddress_StateOrRegion"                                                AS shipping_address_state_or_region
        ,"ShippingAddress_PostalCode"                                                   AS shipping_address_postal_code
        ,"ShippingAddress_City"                                                         AS shipping_address_city
        ,"ShippingAddress_CountryCode"                                                  AS shipping_address_country_code
        ,"IsAccessPointOrder"                                                           AS is_access_point_order 
        ,"SellerOrderId"                                                                AS seller_order_id    
        ,"PaymentMethod"                                                                AS payment_method 
        ,"IsBusinessOrder"                                                              AS is_business_order
        ,"OrderTotal_CurrencyCode"                                                      AS order_total_currency_code
        ,"OrderTotal_Amount"                                                            AS order_total_amount
        ,"PaymentMethodDetails"                                                         AS payment_method_details
        ,"IsGlobalExpressEnabled"                                                       AS is_global_express_enabled
        ,CAST("LastUpdateDate" AS TIMESTAMP)                                            AS last_update_time_stamp   
        ,CAST("LastUpdateDate" AS TIMESTAMP) AT TIME ZONE 'America/Los_Angeles'         AS last_update_time_stamp_la
        ,"ShipmentServiceLevelCategory"                                                 AS shipping_service_level_category
    FROM    
        {{ ref('src_Amz_Orderss') }}
)

SELECT 
    *
FROM
    Load_Data