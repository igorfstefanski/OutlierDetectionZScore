"""
TITLE: OUTLIER DETECTION USING Z SCORE
AUTHOR: Igor Stefański
DATE: April 2022
DESCRIPTION:
Simple outlier detection in two-column dataframe using Z Score.
Function treats a dataframe as a whole and counts mean and std for all values, without column division.
"""


import numpy as np
import pandas as pd


def outliers_detector(dataframe):
    '''
    Returns list of tuples showing 0-based indexes of a row and column of an outliers.
    Args:
        dataframe: dataframe with values
    Returns: list of tuples with row and column index of an outlier
    '''
    outliers_ls = []
    THRESHOLD = 3

    mean = dataframe.values.mean()
    std = dataframe.values.std(ddof=1)

    for i in dataframe:
        counter = 0
        for j in dataframe[i]:
            if std != 0:
                z = (j-mean)/std
            else:
                z = 1

            if z > THRESHOLD:
                temp = (counter, dataframe.columns.get_loc(i))
                outliers_ls.append(temp)

            counter += 1

    return outliers_ls


if __name__ == __main__:
    # example data
    data = {'X1': [155, 15, 13, 11, 12, 11, 15, 156, 13, 10, 12],
            'X2': [149, 169, 172, 148, 156, 162, 189, 555, 147, 150, 153]}

    print(outliers_detector(pd.DataFrame.from_dict(data)))
