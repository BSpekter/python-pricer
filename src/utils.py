import numpy as np
import pandas as pd
import calendar


def thirdwednsday(year, month):
    return calendar.Calendar().monthdatescalendar(year, month)[2][2]


def extract_rates(filepath):
    df = pd.read_csv(filepath, parse_dates=[3, 4])
    index = df.StartDate.apply(lambda x: thirdwednsday(x.year, x.month))
    index[0] = df.StartDate[0]
    df.index = pd.to_datetime(index)
    df['IR'] = 1. - df.iloc[:, 1] / 100
    df.iloc[0, 5] = df.iloc[0, 1]
    df['DF3m'] = np.exp(-df.IR)
    return df.DF3m


def parse_dates(dates: list):
    return [pd.to_datetime(date, format='%d.%m.%y') for date in dates]
