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

def replace_sheet_data(google_sheet_file_id, sheet_name, data):
    sheet = client.open_by_key(google_sheet_file_id).worksheet(sheet_name)

    # Clear the sheet before inserting new data
    sheet.clear()
    sheet.update('A1', data)
    return   f"Data successfully exported to {sheet_name}"




