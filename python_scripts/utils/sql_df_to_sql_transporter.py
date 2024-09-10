import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from .creds import sql_credentials

def export_dataframe_to_postgresql(dataframe, table_name, schema_name):
    """
    Export a Pandas DataFrame to a PostgreSQL table. If the table exists, it will be replaced.
    
    :param dataframe: The Pandas DataFrame to export.
    :param table_name: The name of the table to export to.
    :param schema_name: The schema name where the table should be created.
    :param sql_credentials: A dictionary with keys 'user', 'password', 'host', 'port', 'database' for PostgreSQL connection.
    :return: A message indicating the status of the operation.
    """
    try:
        # Create a connection string
        connection_string = (
        #    f"postgresql://{sql_credentials['user']}:{sql_credentials['password']}@"
         #   f"{sql_credentials['host']}:{sql_credentials['port']}/{sql_credentials['database']}"

            f"postgresql+psycopg2://{sql_credentials['user']}:{sql_credentials['password']}@"
            f"{sql_credentials['host']}:{sql_credentials['port']}/{sql_credentials['database']}"
        )

        # Create a SQLAlchemy engine
        engine = create_engine(connection_string)

        # Use pandas to export the DataFrame to PostgreSQL
        dataframe.to_sql(table_name, con=engine, schema=schema_name, if_exists='replace', index=False)

        return f"Table '{schema_name}.{table_name}' has been created/replaced successfully."
    
    except Exception as e:
        return f"Error exporting DataFrame to PostgreSQL: {e}"
    