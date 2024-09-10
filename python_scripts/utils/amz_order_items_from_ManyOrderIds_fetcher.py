from .amz_order_items_fetcher import OrderItemsFetcher
from .amz_order_item_normalizer import OrderItemsNormalizer
import time

def get_order_items_from_many_orders(order_ids):
    order_items = []
    items_count = 0
    for order in order_ids: 
        attempt = 1
        while attempt <= 4: 
            items, status_code = OrderItemsFetcher(order).GetItem()
            if status_code == 200: 
                items_count += 1
                print(f'fetched order_items of {items_count} orders')
                order_items.extend(items)
                break
            elif attempt ==4: 
                print(f'An error occur! status_code: {status_code}, process stopped!!')
                return order_items, status_code
            else:
                attempt += 1
                print(f'status_code: {status_code}')
                print(f'exceeded rate limit, sleeping for 30  seconds before retry {attempt}th time')
                time.sleep(30)
    print('Finished!!!')
    return order_items
