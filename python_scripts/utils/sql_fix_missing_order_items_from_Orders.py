from .sql_query_executor import SqlQueryExecuter
from .amz_order_items_from_ManyOrderIds_fetcher import get_order_items_from_many_orders
from .amz_order_item_normalizer import OrderItemsNormalizer
from .sql_order_items_to_sql_exporter import OrderItemsToSqlExporter

def fix_missing_order_items():
    sql_query = """ 
                WITH orders AS (
                SELECT 
                    "AmazonOrderId" AS order_id
                FROM 
                    "vne_dtw"."raw_amazon"."Orders"
                ),

                orderitems AS (
                    SELECT 
                        DISTINCT order_id
                    FROM 
                        "vne_dtw"."raw_amazon"."OrderItems"
                ),

                missing_orders AS(
                    
                    SELECT 
                        orders.order_id
                    FROM 
                        orders
                        LEFT JOIN 
                        orderitems
                        ON 
                            orders.order_id = orderitems.order_id
                    WHERE 
                        orderitems.order_id IS NULL	
                )

                SELECT 
                    *
                FROM 
                    missing_orders
                """
    order_ids_tuples = SqlQueryExecuter(sql_query).execute_and_fetch()[0]
    order_ids = [item[0] for item in order_ids_tuples ]
    order_items = get_order_items_from_many_orders(order_ids)
    normalized_order_items = [OrderItemsNormalizer(item, item["order_id"]).normalize() for item in order_items]
    exporter = OrderItemsToSqlExporter(normalized_order_items).export_to_sql()
    print(exporter)
    return normalized_order_items




