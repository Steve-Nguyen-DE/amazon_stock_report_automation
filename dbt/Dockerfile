# Use Python as the base image
FROM python:3.10-slim 

# Set the working directory inside the container
WORKDIR /opt/dbt_vne

# Install DBT and DBT Postgres adapter
RUN pip install dbt-core==1.8.6 dbt-postgres==1.8.2

# Copy the contents of the dbt project folder into /opt/dbt_vne
COPY . /opt/dbt_vne/

# Install any additional dependencies if required
RUN pip install -r requirements.txt

# Make sure dbt is aware of the profiles.yml location
ENV DBT_PROFILES_DIR=/opt/dbt_vne/.dbt/

# add a task to make sure the container is not quitting right after starting
CMD ["tail", "-f", "/dev/null"]

