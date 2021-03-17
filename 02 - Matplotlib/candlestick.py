# imports
import pandas_datareader as data
import pandas as pd
import matplotlib.pyplot as mpl_plt
import matplotlib.dates as mpl_dates
import mplfinance as mpf

'''
This scripts purpose is to plot a candlestick chart
'''

# First day
start_date = '2020-02-01'
# Last day
end_date = '2021-02-28'
# Call the function DataReader from the class data
dataset = data.DataReader('GC=F', 'yahoo', start_date, end_date)

mpf.plot(dataset,type='candle')