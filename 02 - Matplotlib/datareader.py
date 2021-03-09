# imports
import pandas_datareader as data
import pandas as pd

# set print options for console output
pd.set_option('max_rows', 1000)
pd.set_option('max_columns', 1000)
pd.set_option('display.width', 1000)

# First day
start_date = '2020-01-01'
# Last day
end_date = '2021-02-28'
# Call the function DataReader from the class data
dataset = data.DataReader('GC=F', 'yahoo', start_date, end_date)

# Append a new column with difference to previous day
dataset['difference'] = dataset['Close'].diff()

print(dataset)

temp_counter = 0
for x in dataset['difference']:
    if x > 0: temp_counter += 1

print('')
print('Succ: ' + str(temp_counter))
print('Loss: ' + str(len(dataset)-temp_counter))
print('Totl: ' + str(len(dataset)))
