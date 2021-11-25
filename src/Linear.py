import numpy as np


class Linear:
    def __init__(self, X, target):
        tmp = np.array([X, target])
        self.table = tmp[:, tmp[0, :].argsort()]

    def func(self, z):
        x = self.table[0, :]
        y = self.table[1, :]

        right = np.searchsorted(x, z)
        if right == x.shape[0]:
            right -= 1
        elif right == 0:
            right += 1
        
        answer = (y[right] - y[right - 1]) / (x[right] - x[right - 1]) * (z - x[right - 1])
        answer += y[right - 1]
        return answer
