class OrderItemsNormalizer:
    def __init__(self, order_item, order_id):
        self.order_item = order_item
        self.order_id = order_id
        self.normalized_item = {}
    def normalize(self):
        self.normalized_item['order_item_id'] = self.order_item.get('OrderItemId')
        self.normalized_item['order_id'] = self.order_id
        self.normalized_item['asin'] = self.order_item.get('ASIN')
        self.normalized_item['seller_sku'] = self.order_item.get('SellerSKU')
        self.normalized_item['title'] = self.order_item.get('Title')
        self.normalized_item['quantity_ordered'] = self.order_item.get('QuantityOrdered')
        self.normalized_item['quantity_shipped'] = self.order_item.get('QuantityShipped')
        self.normalized_item['item_price_amount'] = self.order_item.get('ItemPrice', {}).get('Amount')
        self.normalized_item['item_price_currency'] = self.order_item.get('ItemPrice', {}).get('CurrencyCode')
        self.normalized_item['item_tax_amount'] = self.order_item.get('ItemTax', {}).get('Amount')
        self.normalized_item['item_tax_currency'] = self.order_item.get('ItemTax', {}).get('CurrencyCode')
        self.normalized_item['promotion_discount_amount'] = self.order_item.get('PromotionDiscount', {}).get('Amount')
        self.normalized_item['promotion_discount_currency'] = self.order_item.get('PromotionDiscount', {}).get('CurrencyCode')
        self.normalized_item['promotion_discount_tax_amount'] = self.order_item.get('ShippingDiscountTax', {}).get('Amount')
        self.normalized_item['promotion_discount_tax_currency'] = self.order_item.get('ShippingDiscountTax', {}).get('CurrencyCode')
        self.normalized_item['is_gift'] = self.order_item.get('IsGift')
        self.normalized_item['is_transparency'] = self.order_item.get('IsTransparency')
        self.normalized_item['tax_collection_model'] = self.order_item.get('TaxCollection', {}).get('Model')
        self.normalized_item['tax_collection_responsible_party'] = self.order_item.get('TaxCollection', {}).get('ResponsibleParty')
        self.normalized_item['product_info_number_of_items'] = self.order_item.get('ProductInfo', {}).get('NumberOfItems')

        return self.normalized_item

