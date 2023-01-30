from sqlalchemy import create_engine
import pandas as pd
from dotenv import dotenv_values
from datetime import datetime
dotenv_values()

def get_database_conn():
    '''
    This function retrieve database credentials from environment variable file (.env)
    and create a connection object used for establishing connection to a postgresql
    database instance.
    Parameter: Does not accept a parameter
    Return value: return a postgresql database connection object
    Return type: Postgresql database obeject
    '''
    # Get database credentials from environment variable
    config = dict(dotenv_values('../.env'))
    db_user_name = config.get('DB_USER_NAME')
    db_password = config.get('DB_PASSWORD')
    db_name = config.get('DB_NAME')
    port = config.get('PORT')
    host = config.get('HOST')
    # Create and return a postgresql database connection object
    return create_engine(f'postgresql+psycopg2://{db_user_name}:{db_password}@{host}:{port}/{db_name}')
    

def validate_date(date_str):
    '''
    This function convert a date string value to a date object. It also checks for date validity
    by converting February 29 to 28 for Non leap years.
    Parameter: Accepts a date string
    Return value: returns a transformed date object.
    Return type: date
    '''
    try:
        return datetime.strptime(date_str, '%m/%d/%Y').date()
    except ValueError:
        return datetime.strptime(date_str.replace('29', '28'), '%m/%d/%Y').date()

def create_analytics_report(query, conn_engine, output_file_name):
    '''
    This function is used to generate analytics report from tables in the 
    database based on specified query logic.
    Parameters:
     - query : The SQL query logic for the report.
     - conn_engine : The is the database connection engine object
     - output_file_name : The name of the created outpufile with it's path.
    Return value: Does not return a value
    Return type: None
    '''
    # Read data from database tables based on query logic
    report = pd.read_sql(query, con = conn_engine, index_col= None)
    # Write report data to an external .xls file
    report.to_excel(output_file_name, index= False)