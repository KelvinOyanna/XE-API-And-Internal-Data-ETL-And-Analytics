from extract_xchange_rates import get_exchange_rates, transform_data

def main():
    # Pull exchange rates data from API
    get_exchange_rates()
    # Transform raw exchange rates data in an external JSON file
    transform_data()

main()