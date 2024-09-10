import gspread
from oauth2client.service_account import ServiceAccountCredentials
import psycopg2
import os
import pandas as pd

import sys

# Google Sheets setup
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

current_dir = os.path.dirname(os.path.abspath(__file__))
json_keyfile_path = os.path.join(current_dir, 'creds_GoogleServiceAccount_key.json')
creds = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile_path, scope)
client = gspread.authorize(creds)

def get_data_from_sheet(google_sheet_file_id, sheet_name):
    # Open the Google Sheet
    sheet = client.open_by_key(google_sheet_file_id).worksheet(sheet_name)

    # Get all values from the sheet as strings
    data = sheet.get_all_values() #use get_all_values instead of get_all_records to treat the "," decimal separator accurately
    return data





