# Use the official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /opt/python_scripts

# Copy the contents of the current directory to /opt/python_scripts
COPY . /opt/python_scripts/

#Modify your Dockerfile to include the PostgreSQL development libraries before running pip install
RUN apt-get update && apt-get install -y libpq-dev gcc

# Install the Python dependencies from requirements.txt located in the copied folder
RUN pip install --no-cache-dir -r /opt/python_scripts/requirements.txt

# List the files in the directory for debugging purposes
RUN ls -la /opt/python_scripts/

#Add a long-running process,  to keep the container running (to avoid exiting immediately after it starts. This behavior is typical for containers that don't have any long-running process keeping them alive)
CMD ["tail", "-f", "/dev/null"]


# Attempt to make the file executable
#RUN chmod +x /opt/python_scripts/run_daily_orders_update.py

# Set the command to execute the script
#CMD ["python3", "/opt/python_scripts/run_daily_orders_update.py"]
