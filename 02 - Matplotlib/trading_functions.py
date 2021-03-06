import numpy as np


# Upday (Close > Open)
def updays(dataset):
    for i, row in dataset.iterrows():
        upday_val = np.nan
        if (row['Close'] > row['Open']):
            upday_val = row['Low'] * 0.99
            dataset.at[i, 'Upday'] = True
            dataset.at[i, 'Upday_Signal'] = upday_val
        else:
            dataset.at[i, 'Upday'] = False

    return dataset


# Append trading range (High - Low)
def tradingrange(dataset):
    for i, row in dataset.iterrows():
        dataset.at[i, 'Range'] = dataset.at[i, 'High'] - dataset.at[i, 'Low']

    return dataset

