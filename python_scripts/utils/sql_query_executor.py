from .creds import sql_credentials
import psycopg2

class SqlQueryExecuter:
    def __init__(self, sql_query):
        self.sql_query = sql_query

    def execute_and_fetch(self):
        try:
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
            
            # Try to fetch data if it's a SELECT query
            try:
                data = cursor.fetchall()
                column_names = [desc[0] for desc in cursor.description]  # Get column names
            except psycopg2.ProgrammingError:
                # No results to fetch (e.g., the query was an INSERT, UPDATE, DELETE)
                data = None
                column_names = None
            
            # Close the cursor and connection
            cursor.close()
            connection.close()
            
            return data, column_names
        
        except Exception as e:
            # Ensure the connection is closed in case of an error
            if connection:
                connection.close()
            return f"An error occurred: {e}", None

# Example usage:
# sql_query = "SELECT * FROM your_table_name;"
# executer = SqlQueryExecuter(sql_query)
# result = executer.execute_and_fetch()
# print(result)
