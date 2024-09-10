from utils.gsheet_get_data_from_sheet import get_data_from_sheet
from utils.sql_df_to_sql_transporter import export_dataframe_to_postgresql
from utils.common_remove_diacritics_Vietnamese import remove_diacritics

import pandas as pd 
import sys


data = get_data_from_sheet('1-eaOBB1t177X-QRgC3KeQq7ZEAniYzrhw-qwu3ooW60', 'Đặt hàng chi tiết')

# since in google sheet the decimal separator is ",", we need to change it to ".":
# Convert the data to a list of dictionaries with proper header mapping

#remove diacritics from columns name since it is in Vietnamese
headers_vietnamese = data[0]  # First row contains headers
headers = []
for header in headers_vietnamese: 
    header_fixed = remove_diacritics(header.strip().lower()).replace(' ', '_').replace('đ', 'd')
    headers.append(header_fixed)

data_records = []

for row in data[1:]:  # Skip the header row
    record = {}
    for i, header in enumerate(headers):
        value = row[i]
        # If the value is a string and contains a comma, replace it with a dot and convert to float
        if header in ['gia_mua_hang', 'gia_tri_dat_hang', 'gia_tri_thuc_xuat']:
            try:
                # Replace comma with dot and convert to float
                record[header] = int(value.replace('.', '').replace(' đ', ''))
            except ValueError:
                # If conversion fails (e.g., for text), keep the original value
                record[header] = value
        else:
            record[header] = value
    data_records.append(record)

df = pd.DataFrame(data_records, columns=headers) # convert data to dataframe
df2 = df[(df['sku'].notna()) & (df['sku'].str.strip() != '')] # removed empty rows

print(len(df2))

exporter = export_dataframe_to_postgresql(df2, "VneAmzPurchasingOrdersDetail", "raw_amazon")
print(exporter)

