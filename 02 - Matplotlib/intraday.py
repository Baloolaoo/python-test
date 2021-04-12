# imports
import pandas as pd
import mplfinance as mpf

# set print options for console output
pd.set_option('max_rows', 1000)
pd.set_option('max_columns', 1000)
pd.set_option('display.width', 1000)

# Read data from csv
dataset = pd.read_csv("../00 - Datasources/dax_m5_2019.csv", index_col=0, parse_dates=True)
dataset = dataset.drop('Volume', axis=1)
dataset.index.name = 'Date'

range_begin = '2019-01-02 08:00:00'
range_end = '2019-01-03 22:00:00'

dataset = dataset.loc[range_begin:range_end, :]

print(dataset)

mpf.plot(dataset, type='candle')
