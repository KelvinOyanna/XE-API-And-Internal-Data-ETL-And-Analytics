import pandas as pd
from util import get_database_conn
from datetime import datetime
from util import validate_date

# Below is an alternative code to download the data directly from the provided links Google sheet links
# Each url can be parsed in the pandas read_csv() method.
# export_format = 'export?format=csv&gid='
# borrower_table_url = f'https://docs.google.com/spreadsheets/d/1mfm4NUfv4wOJfMdjOIA5k99N79JFJDJeTBhzUfIYtzs/{export_format}0'
# loan_table_url = f'https://docs.google.com/spreadsheets/d/16g0zXNzwT6zNtVYVQotaow_mXks2Ervn2LrgPOM6NzI/{export_format}760287896'
# payment_schedule_url = f'https://docs.google.com/spreadsheets/d/1LawsJQtLGpO6AQZFDpgSUEn8A_TVFD9I/{export_format}1692992163'
# loan_payment_url = f'https://docs.google.com/spreadsheets/d/1EP02-iuIEk0FI971A5S4BBzqDeDCr4cB40HZzhOinj4/{export_format}1895216066'

# Create database connection engine
conn_engine = get_database_conn()



def transform_load_to_db():
    '''
    This function extract, transforms and loads data into a Postgresql database.
    Parameter: Does not accept a parameter
    Return value: Doest not return a value
    Return type: None
    '''
    # Extract data for all the tables
    borrower = pd.read_csv('data/Borrower_Data.csv')
    loan = pd.read_csv('data/Loan_Data.csv')
    payment_schedule = pd.read_csv('data/Payment_Schedule.csv')
    loan_payment = pd.read_csv('data/Loan_payment.csv')
    # Transform and load borrower data to a table in the database
    borrower = borrower.loc[:, borrower.columns != 'borrower_credit_score']
    borrower.rename(columns= {'Borrower_Id': 'borrower_id', 'State': 'state', 'City': 'city', 'zip code': 'zip_code'}, inplace=True)
    borrower.to_sql('borrower', con = conn_engine, if_exists = 'append', index = False)

    # Transform and load loan table to database
    loan['Date_of_release'] = loan['Date_of_release'].apply(validate_date)
    loan['Maturity_date'] = loan['Maturity_date'].apply(validate_date)
    loan.rename(columns= {'Borrower_id': 'borrower_id', 'Date_of_release': 'date_of_release', 'Term': 'term', 'InterestRate': 'interest_rate', \
        'LoanAmount': 'loan_amount', 'Downpayment': 'down_payment', 'Payment_frequency': 'payment_frequency', 'Maturity_date': 'maturity_date'}, inplace=True)
    loan.to_sql('loan', con = conn_engine, if_exists = 'append', index = False)

    # Transform and load payment_schedule data to a table in the database
    payment_schedule['Expected_payment_date'] = payment_schedule['Expected_payment_date'].apply(lambda x: datetime.strptime(x, '%m/%d/%Y').date())
    payment_schedule.rename(columns={'Expected_payment_date': 'expected_payment_date', 'Expected_payment_amount' : 'expected_payment_amount'}, inplace=True)
    payment_schedule.to_sql('payment_schedule', con = conn_engine, if_exists = 'append', index = False)

    # Transform and load loan_payment data to a table in the database
    loan_payment.rename(columns= {'loan_id(fk)': 'loan_id', 'payment_id(pk)': 'payment_id', 'Amount_paid': 'date_paid', \
        'Date_paid': 'amount_paid'}, inplace= True)
    loan_payment['date_paid'] = loan_payment['date_paid'].apply(lambda x: datetime.strptime(x, '%m/%d/%Y').date())
    loan_payment.to_sql('loan_payment', con = conn_engine, if_exists = 'append', index = False)
