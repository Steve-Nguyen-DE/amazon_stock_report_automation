import psycopg2
from .creds import sql_credentials

class SqlDataFetcher:
    def __init__(self, sql_query):
        self.sql_query = sql_query

    def fetch_data(self):
        # Establish the database connection
        connection = psycopg2.connect(
            dbname=sql_credentials["database"],
            user=sql_credentials["user"],
            password=sql_credentials["password"],
            host=sql_credentials["host"],
            port=sql_credentials["port"]
        )
        cursor = connection.cursor()

        # Execute the SQL query
        cursor.execute(self.sql_query)
        
        # Fetch the data
        data = cursor.fetchall()
        
        # Fetch column namesn 
        column_names = [desc[0] for desc in cursor.description]
        
        # Close the cursor and connection
        cursor.close()
        connection.close()

        order_ids_list = [item[0] for item in data]
        
        return order_ids_list, column_names

