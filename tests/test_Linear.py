from src.Linear import *
import numpy as np
import matplotlib.pyplot as plt


def my_func(x):
    return x**2 + x - 1


x = np.arange(-10, 10).astype('float')
y = my_func(x)
value_x = -11
value_y = Linear(x, y).func(value_x)
y = np.append(y, value_y)
x = np.append(x, value_x)
order = np.argsort(x)
x = x[order]
y = y[order]
print("error = ", np.abs(value_y - my_func(value_x)))
plt.plot(x, y)
plt.show()
