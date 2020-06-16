'''Libraries'''
import requests
import json
import pandas as pd
import os
from datetime import date

'''Function'''
def get_data(ticker,api_key):
    today = str(date.today())

    if not os.path.isdir('json_data'):
        os.mkdir('json_data')

    headers = {
        'Content-Type': 'application/json'
    }

    file_string = 'json_data/'+ticker+'_'+today+'_data.txt'
    url_string = 'https://api.tiingo.com/tiingo/daily/'+ticker+'/prices?startDate=2019-01-02&token='+api_key
    if not os.path.isfile(file_string):
        requestResponse = requests.get(url_string, headers=headers)
        with open(file_string, 'w') as outfile:
            json.dump(requestResponse.json(), outfile)
    df = pd.read_json (file_string)
    return df

'''Using the function'''
data = get_data('amzn','YourAPIToken')
print(data)

