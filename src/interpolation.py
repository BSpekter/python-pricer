class LinearInterpolator:
    def __init__(self, xs=None, ys=None):
        self.X = xs
        self.Y = ys

    def fit(self, xs, ys):
        self.X = xs
        self.Y = ys

    def interpolate_point(self, x):
        assert self.X is not None, "Fit first"
        ind = self._binsearch(x, 0, len(self.Y) - 1)
        return self._lininterpolate(x, ind)

    def interpolate_array(self, xs):
        # assuming later on log(len(xs)) << len(self)
        perm, xs = zip(*sorted(enumerate(xs), key=lambda x: x[1]))
        ys = []
        ind = 0
        size = len(self.Y) - 1
        for x in xs:
            ind = self._binsearch(x, ind, size)
            ys.append(self._lininterpolate(x, ind))
        return list(zip(*sorted(zip(perm, ys))))[1]

    def _binsearch(self, target, left, right):
        res = left
        if target >= self.X[right]:
            return right - 1
        while left <= right:
            m = (left + right) // 2
            if target < self.X[m]:
                right = m - 1
            else:
                res = m
                left = m + 1
        return res

    def _lininterpolate(self, x, ind, eps=1e-15):
        # since we have prior guarantees that all x_i < x_{i+1}
        # eps value should be small enough for the given context: eps << |x1-x0| for all the pairs
        return self.Y[ind] + (self.Y[ind + 1] - self.Y[ind]) / (self.X[ind + 1] - self.X[ind] + eps) * (x - self.X[ind])
