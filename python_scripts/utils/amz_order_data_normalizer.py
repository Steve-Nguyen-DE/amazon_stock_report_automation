import json

def order_normalize(order):
    fields = {
        'AmazonOrderId': order.get('AmazonOrderId'),
        'BuyerInfo_BuyerEmail': order.get('BuyerInfo', {}).get('BuyerEmail'),
        'EarliestShipDate': order.get('EarliestShipDate'),
        'SalesChannel': order.get('SalesChannel'),
        'OrderStatus': order.get('OrderStatus'),
        'NumberOfItemsShipped': order.get('NumberOfItemsShipped'),
        'OrderType': order.get('OrderType'),
        'IsPremiumOrder': order.get('IsPremiumOrder'),
        'IsPrime': order.get('IsPrime'),
        'FulfillmentChannel': order.get('FulfillmentChannel'),
        'NumberOfItemsUnshipped': order.get('NumberOfItemsUnshipped'),
        'HasRegulatedItems': order.get('HasRegulatedItems'),
        'IsReplacementOrder': order.get('IsReplacementOrder'),
        'IsSoldByAB': order.get('IsSoldByAB'),
        'LatestShipDate': order.get('LatestShipDate'),
        'ShipServiceLevel': order.get('ShipServiceLevel'),
        'IsISPU': order.get('IsISPU'),
        'MarketplaceId': order.get('MarketplaceId'),
        'PurchaseDate': order.get('PurchaseDate'),
        'ShippingAddress_StateOrRegion': order.get('ShippingAddress', {}).get('StateOrRegion'),
        'ShippingAddress_PostalCode': order.get('ShippingAddress', {}).get('PostalCode'),
        'ShippingAddress_City': order.get('ShippingAddress', {}).get('City'),
        'ShippingAddress_CountryCode': order.get('ShippingAddress', {}).get('CountryCode'),
        'IsAccessPointOrder': order.get('IsAccessPointOrder'),
        'SellerOrderId': order.get('SellerOrderId'),
        'PaymentMethod': order.get('PaymentMethod'),
        'IsBusinessOrder': order.get('IsBusinessOrder'),
        'OrderTotal_CurrencyCode': order.get('OrderTotal', {}).get('CurrencyCode'),
        'OrderTotal_Amount': order.get('OrderTotal', {}).get('Amount'),
        'PaymentMethodDetails': order.get('PaymentMethodDetails'),
        'IsGlobalExpressEnabled': order.get('IsGlobalExpressEnabled'),
        'LastUpdateDate': order.get('LastUpdateDate'),
        'ShipmentServiceLevelCategory': order.get('ShipmentServiceLevelCategory'),
    }

    return fields

def orders_normalize(orders):
    normalized_orders = []
    for order in orders: 
        normalized_order = order_normalize(order)
        normalized_orders.append(normalized_order)
    
    return normalized_orders
    