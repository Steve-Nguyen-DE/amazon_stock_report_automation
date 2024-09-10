
from .sql_records_to_sql_transporter import insert_or_update_records_to_a_sql_table
class OrdersToSqlExporter:
    def __init__(self, orders): #order_items is a normalized list of dictionary
        self.orders = [tuple(item.values()) for item in orders] # convert order_item from list to tuple
        self.table_name = '"vne_dtw"."raw_amazon"."Orders"'
        self.columns = (
                "AmazonOrderId",
                "BuyerInfo_BuyerEmail",
                "EarliestShipDate",
                "SalesChannel",
                "OrderStatus",
                "NumberOfItemsShipped",
                "OrderType",
                "IsPremiumOrder",
                "IsPrime",
                "FulfillmentChannel",
                "NumberOfItemsUnshipped",
                "HasRegulatedItems",
                "IsReplacementOrder",
                "IsSoldByAB",
                "LatestShipDate",
                "ShipServiceLevel",
                "IsISPU",
                "MarketplaceId",
                "PurchaseDate",
                "ShippingAddress_StateOrRegion",
                "ShippingAddress_PostalCode",
                "ShippingAddress_City",
                "ShippingAddress_CountryCode",
                "IsAccessPointOrder",
                "SellerOrderId",
                "PaymentMethod",
                "IsBusinessOrder",
                "OrderTotal_CurrencyCode",
                "OrderTotal_Amount",
                "PaymentMethodDetails",
                "IsGlobalExpressEnabled",
                "LastUpdateDate",
                "ShipmentServiceLevelCategory"
                )
        self.conflict_columns = ('AmazonOrderId',)
        
    def export_to_sql(self):
        result = insert_or_update_records_to_a_sql_table(self.table_name, self.columns, self.orders, self.conflict_columns)
        return result