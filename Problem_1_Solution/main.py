from etl import transform_load_to_db
from util import get_database_conn, create_analytics_report

# Create database connection engine
conn_engine = get_database_conn()
output_file_name = f'output/loan_report.xls'
# Query to get report on customers loan performance
loan_report_query = '''
with loan_report as(
select city, zip_code, payment_frequency, maturity_date,
current_date - expected_payment_date as current_days_past_due,
max(expected_payment_date) over(partition by loan_id) as last_due_date,
max(date_paid) over(partition by loan_id) as last_repayment_date,
sum(expected_payment_amount) over(partition by borrower_id order by expected_payment_date rows 
between unbounded preceding and current row) as amount_at_risk,
date_paid - expected_payment_date as par_days
from borrower
join loan using(borrower_id)
join payment_schedule using(loan_id)
join loan_payment using(loan_id)
where date_paid > expected_payment_date
)
select * from loan_report;
'''

def main():
    'Main function for running all other functions/modules.'
    #transform_load_to_db()
    print('All data successfully extracted, transformed and loaded to tables in a postgresql database')
    create_analytics_report(loan_report_query, conn_engine, output_file_name)
    print('Output report data successfully written to external file in directory: output. \n'
    'Please ignore the Warning as the .xls writter module used has been deprecated.')

main()