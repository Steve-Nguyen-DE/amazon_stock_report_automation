from utils.gsheet_decimal_data_sanitizer import sanitize_data
from utils.gsheet_replace_sheet_data import replace_sheet_data
from utils.sql_query_executor import SqlQueryExecuter

sql_query = """ 
            SELECT 
	            *
            FROM 
	            "vne_dtw"."dev_steve"."ana_sales_detail_last_60_days";
            """
data_value, columns = SqlQueryExecuter(sql_query).execute_and_fetch()

data = [tuple(columns)] + data_value
sanitized_data = sanitize_data(data)

sheet_id = '1Kl8I81r8vhNPbzpqPUfdMEMwZhjVpEeTFKk44RMNwuw'
sheet_name = 'orders_last_60_days'

exporter = replace_sheet_data(sheet_id, sheet_name, sanitized_data)
print(exporter)