from sqlalchemy import create_engine
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
    Return type: database obeject
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
    try:
        return datetime.strptime(date_str, '%m/%d/%Y').date()
    except ValueError:
        return datetime.strptime(date_str.replace('29', '28'), '%m/%d/%Y').date()
