import numpy as np
from homework1.Curve import CurveBuilder


m_price = 8
df = 1.1
prices = np.array([["EDM1", m_price*df], ["EDQ1", m_price*df*1.05], ["EDM2", m_price*df*df]])
dates = np.array(["02.06.2022", "05.10.2023", "02.02.2022"])
curve_builder = CurveBuilder(m_price, prices)
r = curve_builder.get_rate_to_dates(dates)
print(r)

