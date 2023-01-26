import pandas as pd
import requests
from dotenv import dotenv_values
dotenv_values()
from xecd_rates_client import XecdClient

# Get API credentials from environment variable file withing the project directory
config = dict(dotenv_values('.env'))
account_id = config.get('ACCOUNT_ID')
api_key = config.get('API_KEY')

def get_exchange_rates(account_id, api_key):
    api_client = XecdClient(account_id, api_key)
    print(api_client.account_info())


get_exchange_rates(account_id, api_key)