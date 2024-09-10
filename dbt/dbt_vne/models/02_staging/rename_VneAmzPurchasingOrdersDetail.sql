WITH Raw_PO_Details AS (
    SELECT 
         ngay_dat                               AS order_date
        ,ma_don_hang                            AS po_id
        ,ma_don_hang_amazon                     AS amazon_shipment_id
        ,sku
        ,fnsku
        ,loai_sp                                AS product_type
        ,ten_sp_me                              AS parent_product_name
        ,loai_hop                               AS box_type
        ,mau_sac                                AS color
        ,sl_fan                                 AS fan_quantity
        ,d                                      AS d_type
        ,chieu_dai                              AS product_length
        ,cong                                   AS curl_type
        ,kt_hop                                 AS box_dimension
        ,sl_thuc_xuat                           AS final_quantity
        ,gia_mua_hang                           AS purchasing_price
        ,gia_tri_dat_hang                       AS po_amount
        ,gia_tri_thuc_xuat                      AS final_po_amount
        ,trang_thai_thanh_toan                  AS order_status
        ,ngay_hang_san_sang                     AS ready_date
        ,trang_thai_thanh_toan                  AS payment_status
        ,ngay_thanh_toan                        AS payment_paid_date
        ,nhap_kho_fba                           AS "imported_to_fba_warehouse"
    FROM
        {{ ref('src_VneAmzPurchasingOrdersDetail') }}
)

SELECT 
    *
FROM 
    Raw_PO_Details