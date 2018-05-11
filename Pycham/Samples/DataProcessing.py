import pandas as pd
#Reading from a csv file
from pandas import DataFrame
import datetime

#import pandas.io.data as web

from pandas_datareader import data
from datetime import datetime
ibm = data.get_data_yahoo(symbols='ibm', start=datetime(2000,1,1), end=datetime(2012,1,1))

#sp500 = web.get_data_yahoo('EBAY',start= datetime.datetime(2000,10,1), end = datetime.datetime(2014,6,11))
print(ibm)
#sp500

