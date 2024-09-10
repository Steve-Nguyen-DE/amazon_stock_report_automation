import requests
from .amz_marketplace_info import endpoint, marketplace_id
from .amz_access_token import get_access_token

class OrderItemsFetcher:
    def __init__(self, orderID):
        self.endpoint_US = endpoint["US"]
        self.access_token = get_access_token()
        self.url = self.endpoint_US  + f"/orders/v0/orders/{orderID}/orderItems"
        self.headers = {
            "x-amz-access-token": self.access_token,
            "Content-Type": "application/json"
        }
        self.orderID = orderID
    def GetItem(self):
        response = requests.get(self.url, headers=self.headers)
        order_items= []
        if response.status_code ==200: 
            order_items = response.json()["payload"]["OrderItems"]
            for item in order_items:
                item['order_id'] = self.orderID
            return order_items, response.status_code
        else:
            print(f'An error occure! status_code : {response.status_code}')
            return order_items, response.status_code