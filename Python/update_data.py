#!/usr/bin/python
# Filename: update_data.py
#
# Update data obtained from CSVs
#
# A cluster is composed by multiples nodes.
# Each of them stores the values of its sensors
# on a CSV file, named with this format:
# DataNode1.csv for Node 1
# This function will read all of the CSV files
# and store its values in a DataFrame structure
# This structured data can be used later to produce
# graphics with plotlyJS


import pandas as pd
from datetime import datetime
import glob


def update_data(path):
    #max_values = int(24 * 60 / 5);
    # To parse the dates stored in columns [1-6] we use this lambda function
    dates_dict = {'date': [1, 2, 3, 4, 5, 6]}
    parse = lambda x: datetime.strptime(x, '%H %M %S %d %m %Y')
    try:
        df = pd.read_csv(path,
                         header=None,
                         parse_dates=dates_dict,
                         date_parser=parse)
    except pd.io.common.EmptyDataError:
        return None
    # Rename the columns
    df.rename(columns={0: 'Sensor', 7: 'Temp', 8: 'Humidity'}, inplace=True)
    # Set the sensor number as index of data frame
    df.set_index(['Sensor'], inplace=True)
    # OPTIONAL
    # FILTER OUTLIERS
    # import numpy as np
    # df = df[np.abs(df.Temp-df.Temp.mean())<=(1*df.Temp.std())]
    #return df.tail(max_values)
    return df


def update_all_data(dirname):
    all_files = glob.glob(dirname + "/DataNode[1-9].csv")
    df = pd.concat([update_data(file_) for file_ in all_files])
    return df
