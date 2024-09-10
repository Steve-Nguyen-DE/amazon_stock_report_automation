import psycopg2
from .creds import sql_credentials

import psycopg2

import psycopg2

import psycopg2

def insert_or_update_records_to_a_sql_table(table_name, table_columns, records_list, conflict_columns=None):
    """
    Insert multiple records into a SQL table, or update if the record already exists.

    :param table_name: The name of the table to insert into.
    :param table_columns: A tuple of column names.
    :param records_list: A list of tuples, each tuple representing a row of values corresponding to the columns.
    :param conflict_columns: A tuple of columns that should be checked for conflicts (e.g., ("order-id", "sku")).
                             If None, performs a simple insert without conflict handling.
    :return: A message indicating the status of the operation.
    """
    try:
        # Establish connection
        connection = psycopg2.connect(
            dbname=sql_credentials["database"],
            user=sql_credentials["user"],
            password=sql_credentials["password"],
            host=sql_credentials["host"],
            port=sql_credentials["port"]
        )
        cursor = connection.cursor()
        
        try:
            # Construct the columns part of the SQL query
            columns = ', '.join([f'"{col}"' for col in table_columns])
            
            # Construct the placeholders for each record
            placeholders = ', '.join(['%s'] * len(table_columns))
            
            # Check if conflict_columns is provided
            if conflict_columns:
                # Construct the conflict column part (for multiple columns)
                conflict_columns_str = ', '.join([f'"{col}"' for col in conflict_columns])
                
                # Construct the update part of the query
                update_columns = ', '.join([f'"{col}" = EXCLUDED."{col}"' for col in table_columns if col not in conflict_columns])
                
                # Construct the full SQL query to insert or update multiple records
                query = f'''
                INSERT INTO {table_name} ({columns}) 
                VALUES ({placeholders}) 
                ON CONFLICT ({conflict_columns_str}) 
                DO UPDATE SET {update_columns}
                '''
            else:
                # If conflict_columns is None, construct a simple insert query
                query = f'''
                INSERT INTO {table_name} ({columns}) 
                VALUES ({placeholders})
                '''
            
            # Execute the query for each record in the records_list
            cursor.executemany(query, records_list)
            connection.commit()  # Commit the transaction
            return f'Inserted/updated {len(records_list)} records into the table {table_name}'
        
        except Exception as e:
            connection.rollback()  # Rollback in case of any error
            return f'Error during insert/update operation: {e}'
        
        finally:
            # Ensure resources are closed
            cursor.close()
            connection.close()

    except Exception as e:
        return f'Error connecting to the database: {e}'
