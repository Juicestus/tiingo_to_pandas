from tiingo_to_pandas import *

ticker = 'aapl'
apiToken = 'YourAPIToken'

data = get_data(ticker,apiToken)

print(data)
