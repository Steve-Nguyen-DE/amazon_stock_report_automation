import requests
import pandas as pd
import psycopg2
from datetime import datetime, timedelta, time
from io import StringIO
import csv
import sys
import os
from .amz_marketplace_info import endpoint, marketplace_id
from .amz_access_token import get_access_token

class ReportIDRequester:
    def __init__(self, dataStartTime, dataEndTime):
        self.endpoint = endpoint #imported from common_importes
        self.marketplace_id = marketplace_id #imported from common_importes
        self.access_token = get_access_token() #imported from common_import
        self.url = self.endpoint["US"] + "/reports/2021-06-30/reports"
        self.headers = {
            "x-amz-access-token": self.access_token,
            "Content-Type": "application/json"
            }   
        self.request_params = {
            "marketplaceIds": [self.marketplace_id["US"]],
            "dataStartTime": dataStartTime,
            "dataEndTime": dataEndTime
        }

    def IDFetcher(self):
        response = requests.post(
            self.url,
            json=self.request_params,
            headers=self.headers
        )

        if response.status_code == 202:
            report_id = response.json()['reportId']
            return report_id, response.status_code
        else:
            # Optionally, handle errors more explicitly
            print("Error fetching orders:", response.status_code, response.text)
            return response.text, response.status_code

class RemovalReportRequester(ReportIDRequester):
    def __init__(self, dataStartTime, dataEndTime):
        super().__init__(dataStartTime, dataEndTime)
        self.request_params["reportType"] = "GET_FBA_FULFILLMENT_REMOVAL_ORDER_DETAIL_DATA"

class ReturnReportRequester(ReportIDRequester):
        def __init__(self, dataStartTime, dataEndTime):
            super().__init__(dataStartTime, dataEndTime)
            self.request_params["reportType"] = "GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA"

def check_report_status(report_id):
    """
    After requesting a report from Amazon, there may be a delay while it is being prepared.
    We need to periodically check the report's status to determine whether the preparation is completed or not
    """
    endpoint_US = endpoint["US"]
    access_token = get_access_token()
    url = endpoint_US + f"/reports/2021-06-30/reports/{report_id}"
    headers = {
        "x-amz-access-token": access_token,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json()
        

class ReportContentFetcher:
    """
    get data from a reportID and convert it to a dataframe
    step 1: Get reportDocumentID
    step 2: Get data from from reportDocumentID
    step 2: Convert data to a dataframe
    """
    def __init__(self, reportId):
        self.access_token = get_access_token()
        self.url = endpoint["US"] + "/reports/2021-06-30/reports/" + str(reportId)
        self.headers = {
                        "Authorization": f"Bearer {self.access_token}",
                        "Content-Type": "application/json",
                        "x-amz-access-token": self.access_token  # sometimes required for specific headers
                        }
        #step 1: get reportDocumentID
    def GetReportContent(self):
        response = requests.get(
                    self.url,
                    headers = self.headers
                    )
        reportDocumentId = response.json()["reportDocumentId"]
        #get file_url
        response = requests.get(
                endpoint["US"] + f"/reports/2021-06-30/documents/{reportDocumentId}", #+ reportID,
                headers = self.headers
            )
        file_url = response.json()["url"]
        # step 2: Get data- Fetch the content from the URL
        response = requests.get(file_url)
        reader = csv.DictReader(StringIO(response.text), delimiter='\t')
        converted_content = list(reader)
        return converted_content


