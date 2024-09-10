WITH Load_Data AS (
    SELECT 
        "SKU Mẹ" AS parent_sku
        ,"ASIN Mẹ" AS parent_asin
        ,"Tên SP Mẹ" AS parent_product_name
        ,"SKU"AS sku
        ,"FNSKU" AS fnsku
        ,"ASIN" AS asin
        ,"Loại SP" AS product_type
        ,"Loại hộp" AS box_type
        ,"Màu Sắc"  AS color
        ,"SL Fan" AS fan_quantity
        ,"D" AS d 
        ,"Length" AS product_length 
        ,"Curl" AS curl
        ,"Tên SP" AS product_name 
        ,"KT Hộp" AS box_dimension
        ,"Phí FBA" AS fba_fee
        ,"Giá đầu vào" AS purchasing_price
        ,"Phí ship VN-US" AS shipping_cost_vn_us
        ,"Giá bán" AS retail_price
    FROM 
        {{ ref('src_VneAmzProducts') }}
)

SELECT 
    *
FROM 
    Load_Data
