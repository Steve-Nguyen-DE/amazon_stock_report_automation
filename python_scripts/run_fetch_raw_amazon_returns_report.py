from utils.sql_query_executor import SqlQueryExecuter
from datetime import datetime, timezone, timedelta
from utils.sql_records_to_sql_transporter import insert_or_update_records_to_a_sql_table
from utils.amz_report_fetcher import  check_report_status, ReportContentFetcher, ReturnReportRequester
import time

sql_query = """
            SELECT 
                MAX("return-date")
            FROM 
                "vne_dtw"."raw_amazon"."Returns"
            """

values, columns = SqlQueryExecuter(sql_query).execute_and_fetch()
start_date = datetime.fromisoformat(values[0][0]) + timedelta(seconds=1)

# Get the current time
current_time = datetime.now()

# Subtract 30 minutes
time_30_mins_ago = current_time - timedelta(minutes=30)

# Define the timezone offset (-07:00)
offset = timezone(timedelta(hours=-7))

# Apply the timezone to the datetime object
time_30_mins_ago_with_time_zone = time_30_mins_ago.replace(tzinfo=offset)

# Format to the desired string format
time_30_mins_ago_formated = time_30_mins_ago_with_time_zone.strftime("%Y-%m-%dT%H:%M:%S%z")

# Insert colon in timezone part (e.g., -0300 to -03:00)
end_date = time_30_mins_ago_formated[:-2] + ':' + time_30_mins_ago_formated[-2:]

response = ReturnReportRequester(start_date, end_date).IDFetcher()
report_id = response[0]

table_name = '"vne_dtw"."raw_amazon"."Returns"'
columns  = (
            "return-date",
            "order-id",
            "sku",
            "asin",
            "fnsku",
            "product-name",
            "quantity",
            "fulfillment-center-id",
            "detailed-disposition",
            "reason",
            "status",
            "license-plate-number",
            "customer-comments"
            )

max_retries = 60  # Adjust as needed, e.g., 60 retries with a 5-second interval is 5 minutes
retry_count = 0
retry_sleep = 5  # Sleep duration between retries (in seconds)

try:
    # Fetch the report ID
    response = ReturnReportRequester(start_date, end_date).IDFetcher()
    report_id = response[0]

    # Loop to check report status with retry mechanism
    while retry_count < max_retries:
        try:
            report_status = check_report_status(report_id)
        except Exception as e:
            print(f"Error checking report status: {e}")
            break

        if report_status["processingStatus"] == 'DONE':
            try:
                report_content = ReportContentFetcher(report_id).GetReportContent()
                records_list = [tuple(item.values()) for item in report_content]

                # Insert or update the records in the database
                try:
                    exporter = insert_or_update_records_to_a_sql_table(table_name, columns, records_list)
                    print(exporter)
                except Exception as e:
                    print(f"Error inserting/updating records to SQL: {e}")
                
                break  # Exit loop when the report is successfully processed

            except Exception as e:
                print(f"Error fetching report content: {e}")
                break

        elif report_status["processingStatus"] == 'FATAL':
            print("Report was broken, report status: 'FATAL'")
            break

        else:
            retry_count += 1
            print(f"Report status is {report_status['processingStatus']}, retrying... ({retry_count}/{max_retries})")
            time.sleep(retry_sleep)  # Wait before retrying

    if retry_count >= max_retries:
        print(f"Max retries reached ({max_retries}), exiting.")

except Exception as e:
    print(f"Unexpected error occurred: {e}")