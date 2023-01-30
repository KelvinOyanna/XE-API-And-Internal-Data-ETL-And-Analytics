from extract_xchange_rates import get_exchange_rates, transform_data
from util import get_api_credentials

# API credentials
account_id = get_api_credentials()[0]
api_key = get_api_credentials()[1]

def main():
    # Pull exchange rates data from API
    get_exchange_rates(account_id, api_key)
    # Transform raw exchange rates data from an external JSON file
    transform_data()
    print('Transformed data written to a csv file')

main()