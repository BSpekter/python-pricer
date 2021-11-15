import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys
sys.path.append('../')
import datetime

class discount_factors_curve(object):
    def __init__(self)
        
#     @staticmethod
    def discount_factors_array(self, dates):
        data = pd.DataFrame(index = dates)
        data['dates'] = np.nan
        last_erodollar = 100 #Костылецкий
        USD_rates = pd.read_csv('../data/USD rates.csv')
        now = datetime.date.today()
        USD_rates.index = USD_rates.EndDate
        USD_rates = USD_rates['Unnamed: 1']
        USD_rates[USD_rates.index[0]] = last_erodollar
        tmp = np.exp(np.log(USD_rates).diff())
        rates = tmp[tmp.index[2]:tmp.index[-1]]
        rates = 1 / rates
        rates = np.exp(np.log(rates).expanding().sum())
        rates.index = pd.to_datetime(rates.index)
        data.index = pd.to_datetime(data.index)
        for_plotting = pd.concat([rates, data],axis=0).drop(['dates'],axis=1).sort_index()
        for_plotting = pd.DataFrame(for_plotting)

        for_plotting.index = pd.to_datetime(for_plotting.index)

        for_plotting['interpolation'] = for_plotting.interpolate(method='time')
        return 1 / for_plotting['interpolation'][dates]
    
    
def discount_factors_array(dates):
        data = pd.DataFrame(index = dates)
        data['dates'] = np.nan
        last_erodollar = 100 #Костылецкий
        USD_rates = pd.read_csv('../data/USD rates.csv')
        now = datetime.date.today()
        USD_rates.index = USD_rates.EndDate
        USD_rates = USD_rates['Unnamed: 1']
        USD_rates[USD_rates.index[0]] = last_erodollar
        tmp = np.exp(np.log(USD_rates).diff())
        rates = tmp[tmp.index[2]:tmp.index[-1]]
        rates = 1 / rates
        rates = np.exp(np.log(rates).expanding().sum())
        rates.index = pd.to_datetime(rates.index)
        data.index = pd.to_datetime(data.index)
        for_plotting = pd.concat([rates, data],axis=0).drop(['dates'],axis=1).sort_index()
        for_plotting = pd.DataFrame(for_plotting)

        for_plotting.index = pd.to_datetime(for_plotting.index)

        for_plotting['interpolation'] = for_plotting.interpolate(method='time')
        return 1 / for_plotting['interpolation'][dates]