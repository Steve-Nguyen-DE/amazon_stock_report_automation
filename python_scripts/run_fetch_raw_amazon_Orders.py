from utils.sql_query_executor import SqlQueryExecuter
from datetime import datetime, timezone, timedelta
from utils.amz_orders_fetcher import LongPeriodOrdersFetcher
from utils.amz_order_data_normalizer import orders_normalize
from utils.amz_order_items_from_ManyOrderIds_fetcher import get_order_items_from_many_orders
from utils.amz_order_item_normalizer import OrderItemsNormalizer
from utils.sql_order_items_to_sql_exporter import OrderItemsToSqlExporter
from utils.sql_orders_to_sql_exporter import OrdersToSqlExporter

#Get latest LatestUpdateDate in database:
sql_query = """
            SELECT 
                MAX("LastUpdateDate")
            FROM 
                "vne_dtw"."raw_amazon"."Orders";
            """
latest_LastUpdateDate = SqlQueryExecuter(sql_query).execute_and_fetch()[0][0][0]
LastUpdatedAfter = latest_LastUpdateDate

# Retrieve the current time and subtract 30 minutes to account for potential time discrepancies.
# Amazon requires the time to be at least 2 minutes earlier than the current time to avoid invalid submissions.
adjusted_time = datetime.now(timezone.utc)- timedelta(minutes=30)
LastUpdatedBefore = adjusted_time.strftime('%Y-%m-%dT%H:%M:%SZ')

#fetching orders from amazon with the aboved time
orders = LongPeriodOrdersFetcher(LastUpdatedAfter, LastUpdatedBefore).GetOrdersInLongPeriod()
normalized_orders = orders_normalize(orders) # normalize nested data inside each order


# Start get and export order_items to database
order_ids_list = [item["AmazonOrderId"] for item in normalized_orders]
order_items = get_order_items_from_many_orders(order_ids_list)
normalized_items = [OrderItemsNormalizer(item, item["order_id"]).normalize() for item in order_items]

print(f'there are totally {len(normalized_orders)} orders fetched')

print('start exporting orders')
orders_exporter = OrdersToSqlExporter(normalized_orders).export_to_sql()
print(orders_exporter)

print('start exporting order_items')
order_items_exporter = OrderItemsToSqlExporter(normalized_items).export_to_sql()
print(order_items_exporter)




