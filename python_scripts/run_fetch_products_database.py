from utils.gsheet_get_data_from_sheet import get_data_from_sheet
from utils.sql_df_to_sql_transporter import export_dataframe_to_postgresql
import pandas as pd 
import sys


data = get_data_from_sheet('1Dedo997CfxeK2gZMxCPEHLMojPOLbtb_f9Lppob3Fy4', 'Producst data Source')

# since in google sheet the decimal separator is ",", we need to change it to ".":
# Convert the data to a list of dictionaries with proper header mapping
headers = data[0]  # First row contains headers
data_records = []

for row in data[1:]:  # Skip the header row
    record = {}
    for i, header in enumerate(headers):
        value = row[i]
        # If the value is a string and contains a comma, replace it with a dot and convert to float
        if header in ['Phí FBA', 'Giá đầu vào', 'Phí ship VN-US', 'Giá bán']:
            try:
                # Replace comma with dot and convert to float
                record[header] = float(value.replace(',', '.'))
            except ValueError:
                # If conversion fails (e.g., for text), keep the original value
                record[header] = value
        else:
            record[header] = value
    data_records.append(record)

df = pd.DataFrame(data_records, columns=headers) # convert data to dataframe
df2 = df[(df['SKU'].notna()) & (df['SKU'].str.strip() != '')] # removed empty rows

print(len(df2))

exporter = export_dataframe_to_postgresql(df2, "VneAmzProducts", "raw_amazon")
print(exporter)

