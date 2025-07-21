
import pandas as pd 
#price = pd.read_pickle('examples/yahoo_price.pkl')
#volume = pd.read_pickle('examples/yahoo_volume.pkl')

import pandas_datareader.data as web


all_data = {ticker: web.get_data_yahoo(ticker) 
     for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}

price = pd.DataFrame({ticker: data['Adj Close']
                     for ticker, data in all_data.items()})
volume = pd.DataFrame({ticker: data['Volume']
                      for ticker, data in all_data.items()})

print(price.shape)
print(volume.shape)

