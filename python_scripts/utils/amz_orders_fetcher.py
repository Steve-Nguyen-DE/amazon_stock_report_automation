import requests
from .amz_marketplace_info import endpoint, marketplace_id
from .amz_access_token import get_access_token
from datetime import datetime, timedelta
import time

class OrdersFetcher:
    def __init__(self, LastUpdatedAfter, LastUpdatedBefore):
        self.LastUpdatedAfter = LastUpdatedAfter
        self.LastUpdatedBefore = LastUpdatedBefore
        self.access_token = get_access_token()
        self.url = endpoint["US"] + "/orders/v0/orders"
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
            "x-amz-access-token": self.access_token  # sometimes required for specific headers
        }
        self.request_params = {
                "LastUpdatedAfter": self.LastUpdatedAfter,
                "LastUpdatedBefore": self.LastUpdatedBefore,
                "MarketplaceIds": [marketplace_id["US"]]
            }
        self.all_orders = []
        
    def GetOrders(self):
        for attempt in range(1,4):
            response = requests.get(
                                    self.url,
                                    headers=self.headers,
                                    params=self.request_params 
                                    )
            if response.status_code == 200:
                data = response.json()
                orders = data.get('payload', {}).get('Orders', [])
#                print(orders[1])
                self.all_orders.extend(orders)
                
                # Check if there is next page
                next_token = data.get('payload', {}).get('NextToken', None)
                print(f"next_token: {next_token}")
                if next_token:
                    self.request_params["NextToken"] = next_token  # Use the NextToken to get the next page
                else:
                    # No more pages
                    break
            elif response.status_code == 429: 
                if attempt == 3:
                    print('Quota Exceeded, process stopped after 3 attempts, try again later!')
                    return self.all_orders, response.status_code, response.text
                else:
                    print(f"Quota Exceeded, retry {attempt+1}th times in 3 mins ")
                    attempt += 1
                    time.sleep(3*60)

            else:
                # Optionally, handle errors more explicitly
                print("Error fetching orders from")
                print(response.status_code)
                print(response.text)
                break
            
        if not self.all_orders : #check if all_orders is empty
            print(f'there is no orders in this period from {self.LastUpdatedAfter} to {self.LastUpdatedBefore}')
    
        print('chunk finished')

        return self.all_orders, response.status_code
            
class LongPeriodOrdersFetcher(OrdersFetcher):
    """
    Amazon typically allows order retrieval for periods no longer than 7 days.
    Therefore, if the time period exceeds 7 days, the function fetch_orders_in_a_time_period will not work as intended.
    To handle longer periods, we need to divide the request into smaller chunks, each covering a period of less than 7 days.
    """
    def GetOrdersInLongPeriod(self):
        current_start = datetime.strptime(self.LastUpdatedAfter, '%Y-%m-%dT%H:%M:%SZ')
        end_time = datetime.strptime(self.LastUpdatedBefore, '%Y-%m-%dT%H:%M:%SZ')
        chunk = 1
        while current_start < end_time:
            current_end = min(current_start + timedelta(days=7), end_time)
            print(f'fetching data from {current_start} and {current_end}')
            self.request_params["LastUpdatedAfter"] =  current_start.strftime('%Y-%m-%dT%H:%M:%SZ')
            self.request_params["LastUpdatedBefore"] = current_end.strftime('%Y-%m-%dT%H:%M:%SZ')
            orders, status_code = self.GetOrders()
            print("Status Code:", status_code)

            if status_code !=200:
                return print('An error occur!')
            else:
                print(f'{chunk} chunk fetched succesfully!')
                self.request_params.pop("NextToken", None) # Pop NextToken out of the request_params to make sure it is not repeated in the next chunk
                chunk += 1

            current_start = current_end
            print('sleeping for 5 seconds to avoid exceed rate limit')
            time.sleep(5)
        
        return self.all_orders

