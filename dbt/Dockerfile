# Use Python as the base image
FROM python:3.10-slim 

# Set the working directory inside the container
WORKDIR /opt/dbt_vne

# Install necessary packages, including git and PostgreSQL development headers
RUN apt-get update && apt-get install -y git build-essential libpq-dev

# Initialize the Git repository
RUN git init

# Add the remote origin (replace with your repository)
RUN git remote add origin https://github.com/Steve-Nguyen-DE/amazon_stock_report_automation.git

# Enable sparse checkout
RUN git config core.sparseCheckout true

# Specify the folder to checkout (in this case, only the dbt/ folder)
RUN echo "dbt/" >> .git/info/sparse-checkout

# Pull the main branch from the repository (this step fetches the dbt folder)
RUN git pull origin main

# Change the working directory to the dbt folder
WORKDIR /opt/dbt_vne/dbt

# Install dbt and other dependencies using the requirements.txt from the dbt folder
RUN pip install --no-cache-dir -r requirements.txt


# Make sure dbt is aware of the profiles.yml location
ENV DBT_PROFILES_DIR=/opt/dbt_vne/dbt/.dbt/

# add a task to make sure the container is not quitting right after starting
CMD ["tail", "-f", "/dev/null"]

