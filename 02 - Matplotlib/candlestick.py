# imports
import pandas_datareader as data
import pandas as pd
import numpy as np
import mplfinance as mpf

'''
This scripts purpose is to plot a candlestick chart out of a pandas dataframe.
Next To-Do:
    - Move 'upday'-loop to function
    - Add functions for
        - Inside days
        - Outside days
    - Plot Inside/Outside days in chart
'''

# set print options for console output
pd.set_option('max_rows', 1000)
pd.set_option('max_columns', 1000)
pd.set_option('display.width', 1000)

# First day
start_date = '2021-01-01'
# Last day
end_date = '2021-02-28'
# Call the function DataReader from the class data
dataset = data.DataReader('GC=F', 'yahoo', start_date, end_date)

# Upday (Close > Open)
for i, row in dataset.iterrows():
    upday_val = np.nan
    if (row['Close'] > row['Open']):
        upday_val = row['Low']*0.99
        dataset.at[i, 'Upday'] = True
        dataset.at[i,'Upday_Signal'] = upday_val
    else:
        dataset.at[i, 'Upday'] = False

apd = mpf.make_addplot(dataset['Upday_Signal'], type='scatter',markersize=100,marker='^', color='r')

print(dataset)

mpf.plot(dataset,type='candle',addplot=apd)
