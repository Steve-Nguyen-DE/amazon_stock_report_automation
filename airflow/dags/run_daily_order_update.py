from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 9, 1, 0, 30),  # Start at 00:30 UTC on September 1, 2024
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'run_daily_order_update_dag',
    default_args=default_args,
    description='A DAG to run the run_daily_order_update.py script manually',
    schedule_interval= '0 */2 * * *',  # Run every 2 hours
    catchup=False,  # Disable catchup for past dates
)

# Define the task
fetch_raw_amazon_Orders = BashOperator(
    task_id='run_daily_order_update_task',
    bash_command='docker exec python-scripts-container python3 /opt/python_scripts/run_fetch_raw_amazon_Orders.py',
    dag=dag,
)

fetch_raw_amazon_removal_report = BashOperator(
    task_id='run_fetch_raw_amazon_removal_report',
    bash_command='docker exec python-scripts-container python3 /opt/python_scripts/run_fetch_raw_amazon_removal_report.py',
    dag=dag,
)

fetch_raw_amazon_PurchasingOrdersDetail = BashOperator(
    task_id='run_fetch_raw_amazon_PurchasingOrdersDetail',
    bash_command='docker exec python-scripts-container python3 /opt/python_scripts/run_fetch_raw_amazon_PurchasingOrdersDetail.py',
    dag=dag,
)

dbt_run = BashOperator(
    task_id='dbt_run',
    bash_command='docker exec dbt_container dbt run --project-dir /opt/dbt_vne/dbt/dbt_vne/',
    dag=dag,
)



update_stock_to_sheet = BashOperator(
    task_id='run_fetch_update_stock_to_sheet',
    bash_command='docker exec python-scripts-container python3 /opt/python_scripts/run_fetch_update_stock_to_sheet.py',
    dag=dag,
)

update_gsheet_details_sales_last_60_days = BashOperator(
    task_id='update_gsheet_details_sales_last_60_days',
    bash_command='docker exec python-scripts-container python3 /opt/python_scripts/run_update_gsheet_details_sales_last_60_days.py',
    dag=dag,
)



# Set the task in the DAG
# Set task dependencies
[fetch_raw_amazon_Orders, fetch_raw_amazon_removal_report, fetch_raw_amazon_PurchasingOrdersDetail] >> dbt_run
dbt_run >> update_stock_to_sheet >> update_gsheet_details_sales_last_60_days