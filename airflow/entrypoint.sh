#!/bin/bash
# Initialize the Airflow database
airflow db init

# Create an admin user if not already created
airflow users create \
  --username admin \
  --password admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com

# Start the Airflow webserver and scheduler together in the background
airflow scheduler &   # Run scheduler in the background
exec airflow webserver # Run webserver in the foreground