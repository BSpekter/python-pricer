import numpy as np
from datetime import datetime
from homework1.Linear import Linear


class CurveBuilder:
    def __init__(self, s_0, prices, date_str="%d.%m.%Y", start_str="1.01.2021"):
        self.month_encode = {'F': 1, 'G': 2, 'H': 3, 'J': 4, 'K': 5, 'M': 6,
                             'N': 7, 'Q': 8, 'U': 9, 'V': 10, 'X': 11, 'Z': 12}
        self.date_str = date_str
        self.start_str = start_str

        start_day = datetime.strptime(start_str, date_str)
        cur_days = [self.__deliver_date(s, start_day.year) for s in prices[::, 0]]
        days_count = [(d - start_day).days for d in cur_days]
        order = np.argsort(days_count)
        days_count = np.sort(days_count)
        values = prices[order, 1].astype(float)
        rates = np.log(values) - np.log(s_0)
        rates /= days_count
        self.linear = Linear(days_count, rates)

    def get_rate_to_dates(self, dates):
        count_days = np.array([self.__count_days_str(self.start_str, date, self.date_str) for date in dates])
        rates = np.array([self.linear.func(counts) for counts in count_days])
        return rates*count_days + 1

    def __count_days_str(self, str1, str2, date_str):
        return (datetime.strptime(str2, date_str) - datetime.strptime(str1, date_str)).days

    def __deliver_date(self, date_str, start_year):
        a, b = self.__date_pars(date_str)
        return datetime.strptime("01.{0:02d}.{1:02d}".format(a, b + start_year), "%d.%m.%Y")

    def __date_pars(self, date_str):
        size = len(date_str)
        month_number = self.month_encode[date_str[size - 2]]
        year_number = int(date_str[size - 1])
        return month_number, year_number
