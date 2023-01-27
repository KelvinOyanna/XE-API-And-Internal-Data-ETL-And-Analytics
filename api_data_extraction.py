import pandas as pd
import requests
import json
import os
from datetime import datetime
from dotenv import dotenv_values
from util import check_last_updated
dotenv_values()

# Get API credentials from environment variable file withing the project directory
config = dict(dotenv_values('.env'))
account_id = config.get('ACCOUNT_ID')
api_key = config.get('API_KEY')

def get_exchange_rates(account_id, api_key):
    '''
    This function sends request and retrieve exchnage rate data from XE REST API.
    Parameter: Takes in two parameters - XE account ID and API key
    Return value: Returns the exchange rate data
    Return type: a dictionary
    '''
    # file_name = f'xrates_{datetime.now().date()}.json'
    # file_path = './raw'
    to_cur = ["NGN", "GHS", "KSH", "USH", "MAD", "CFA", "EGP"]
    url = 'https://xecdapi.xe.com/v1/convert_from.json/?from=USD&to=NGN,GHS,KSH,USH,MAD,CFA,EGP&amount=1'
    
    try: # A try-except block to handle error authenticating or retrieving data from the API
        response = requests.get(url=url, auth= (account_id, api_key))
        response_data = response.json()
        try: # A try-except block to handle error due to directory not available
            if os.path.exists('./raw/exchange_rates_data.json'):
                with open('raw/exchange_rates_data.json', 'r+') as xrates_file:
                    records = json.load(xrates_file)
                    if isinstance(records, dict):
                        updated_records = list(records)
                    else:
                        updated_records = records
                    if check_last_updated(updated_records, response_data):
                        updated_records.append(response_data)
                        xrates_file.seek(0)
                        xrates_file.write('[ \n')
                        for index, item in enumerate(updated_records):
                            if index != (len(updated_records) -1):
                                json.dump(item, xrates_file)
                                xrates_file.write(',\n')
                            else:
                                json.dump(item, xrates_file)
                                xrates_file.write('\n')
                        xrates_file.write(']')
                        print('exchange rate data successfully updated')
                    else:
                        pass
            else:
                with open('raw/exchange_rates_data.json', 'w') as xrates_file:
                    json.dump(response_data, xrates_file)
                    print('exchange rate data successfully written to a file')
        except FileExistsError:
            print('Directory does not exist')
    except requests.exceptions.RequestException as err:
        print(f'Unable to get data from API. Error: {err}')


get_exchange_rates(account_id, api_key)

def transform_data():
    #with
    rates_data = get_exchange_rates(account_id, api_key)
    pass

# update = "2023-01-27T00:00:00Z"
# last_update = datetime.strptime(update, '%Y-%m-%dT%H:%M:%SZ').date()
# print(last_update)