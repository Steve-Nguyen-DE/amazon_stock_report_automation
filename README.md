Project Overview
This project leverages Python, Airflow, and dbt to automate the process of retrieving data from Amazon Seller Central (orders, removals, and returns) and Google Sheets (purchasing information). The data is then transformed and used to generate a real-time stock report.

Project Structure:
python_scripts: This folder contains all scripts responsible for sourcing data from the Amazon Seller API and Google Sheets, as well as pushing data from PostgreSQL to Google Sheets.

dbt: This directory holds all dbt models used for transforming the raw data into usable formats.

airflow: Contains all Airflow DAGs used to schedule and manage the execution of Python scripts and dbt jobs.
