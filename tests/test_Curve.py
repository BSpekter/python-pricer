from src.Curve import *
import matplotlib.pyplot as plt

curve = CurveBuilder("../data/USD rates.csv")
dates, val = curve.make_fixed_leg_fra()
curve.set_linear()
x, y = curve.get_linear(["4/15/21", "11/15/21"])
plt.plot(dates, val)
plt.plot(x, y)
x, y = curve.get_linear(["6/15/22", "12/15/22"])
plt.plot(x, y)
x, y = curve.get_linear(["8/15/24", "10/15/24"])
plt.plot(x, y)
plt.show()
