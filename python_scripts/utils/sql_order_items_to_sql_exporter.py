from .sql_records_to_sql_transporter import insert_or_update_records_to_a_sql_table
class OrderItemsToSqlExporter:
    def __init__(self, order_items): #order_items is a normalized list of dictionary
        self.order_items = [tuple(item.values()) for item in order_items] # convert order_item from list to tuple
        self.table_name = '"vne_dtw"."raw_amazon"."OrderItems"'
        self.columns = (
                        "order_item_id",
                        "order_id",
                        "asin",
                        "seller_sku",
                        "title",
                        "quantity_ordered",
                        "quantity_shipped",
                        "item_price_amount",
                        "item_price_currency",
                        "item_tax_amount",
                        "item_tax_currency",
                        "promotion_discount_amount",
                        "promotion_discount_currency",
                        "promotion_discount_tax_amount",
                        "promotion_discount_tax_currency",
                        "is_gift",
                        "is_transparency",
                        "tax_collection_model",
                        "tax_collection_responsible_party",
                        "product_info_number_of_items",
                    )
        self.conflict_column = ('order_item_id',)
    def export_to_sql(self):
        result = insert_or_update_records_to_a_sql_table(self.table_name, self.columns, self.order_items, self.conflict_column)
        return result