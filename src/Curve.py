import pandas as pd
from src.Linear import *


class CurveBuilder:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = None
        self.percent = 100
        self.days_in_year = 360
        self.table = None
        self.linear = None
        self.start_date = None
        self.dates = None

    def load_csv(self):
        data = pd.read_csv(self.file_name)
        data['EndDate'] = pd.to_datetime(data['EndDate'], format="%m/%d/%y")
        data['StartDate'] = pd.to_datetime(data['StartDate'], format="%m/%d/%y")
        data['Actual_360'] = (data['EndDate'] - data['StartDate']).dt.days / self.days_in_year
        self.data = data

    def calc_libor(self):
        self.data['Libor rate'] = 1 - self.data.iloc[1::, 1] / self.percent
        self.data.iloc[0, 6] = self.data.iloc[0, 1]

    def calc_fra(self):
        self.data.iloc[0, 2] = 0
        self.data['Forward rate'] = self.data['Libor rate'] - self.data['Conv, adj']

    def make_fixed_leg_fra(self):
        self.load_csv()
        self.calc_libor()
        self.calc_fra()
        days_count = self.data['Actual_360']
        fixed_leg = self.data['Forward rate'] \
            * (1 + self.data['Libor rate'] * days_count) / days_count - self.data['Libor rate']
        fixed_leg = fixed_leg.values
        self.dates = self.data['StartDate']
        self.table = (self.dates, fixed_leg)
        return self.table

    def set_linear(self):
        self.start_date = self.dates[0]
        x = (self.dates - self.start_date).dt.days.values
        print(x)
        self.linear = Linear(x, self.table[1][::])

    def get_linear(self, dates_str, format_str="%m/%d/%y"):
        dates = pd.to_datetime(dates_str, format=format_str)
        x = (dates - self.start_date).days
        print(x)
        y = [self.linear.func(z) for z in x]
        return dates, y
